# -*- coding: cp1252 -*-
from django.shortcuts import render
from django.utils import timezone
from .models import Post, Soggetto, Gara, Azienda
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, SoggetoForm, GaraForm, AziendaForm
from django.shortcuts import redirect
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse

# -*- coding: cp1252 -*-

from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import  inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'compilaGare/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'compilaGare/post_detail.html', {'post': post})



def drag(request):
    return render(request, 'compilaGare/drag.html', {'post': ''})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('compilaGare.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'compilaGare/post_edit.html', {'form': form})


def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "sdvsdvdsvsdv world.")

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


from reportlab.lib.pagesizes import letter, A4

class MyPrint:
    def __init__(self, buffer, pagesize):
        self.buffer = buffer
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
        self.width, self.height = self.pagesize
        
    def genera_pdf(self):

    # Create the HttpResponse object with the appropriate PDF headers.
        buffer = self.buffer
        
        p = canvas.Canvas(buffer)
        
        doc = SimpleDocTemplate(buffer,pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)
    
        Story=[]
        titolo = 'Offerta'
        sottotitolo = '(redatta in conformita allALLEGATO T)'
        indirizzo = ['nomeinfirizzo', 'via_inrizzo', 'luogo_indirizzo']
        oggetto = 'OGGETTO: Dichiarazione Personale relativa ai soggetti in carica con poteri di rappresentanza, direttore tecnico, soci, amministratori.'  
        gara_testo = """Codice Esigenza n. 028712  Procedura aperta per la progettazione e l'esecuzione dei lavori di
        RISTRUTTURAZIONE EDILIZIA CON ADEGUAMENTO ALLE NORME SISMICHE DEGLI EDIFICI 1404 E 1404 BIS Localita': Roma -
        Caserma Ettore Rosso.Importo lordo a base di gara 874.175,32 di cui  41.607,00 per oneri per l'attuazionedel piano di sicurezza
        non soggetti a ribasso,  271.670,14 per costo del personale suilavori non soggetto a ribasso (art. 82 c. 3 bis D.Lgs. 163/2006),  10.708,59
        per oneri per la progettazione soggetti a ribasso ed  2.745,30 per costo del personale
        sullaprogettazione non soggetto a ribasso (art. 82 c. 3 bis D.Lgs. 163/2006)."""
        dichiarazione_soggetto_testo = u"""La sottoscritta Impresa Pinco Pallino S.r.l., con sede in Via Tizio Caio n. 1, 00100 Roma,Codice Fiscale e Partita IVA n. 012345678, Tel. 012345678, Fax 012345678, PEC pincopallino@legaltizio.it, e per essa il Sig. Pinco Caio, nato a Roma il 01.01.1985, e residente in Via Tizio n. 1, 00100 Roma, in qualità di Amministratore Unico e Legale Rappresentante pienamente consapevole della responsabilità penale cui va incontro, ai sensi e per gli effetti dell’art. 76 D.P.R. 28 dicembre 2000 n. 445, in caso di dichiarazioni mendaci o di formazione, esibizione o uso di atti falsi, ovvero di atti contenenti dati non più rispondenti a verità,"""
        dichiara = 'dichiara'
        primo_elenco = [u"""di possedere tutti i requisiti d'ordine generale di cui all'art. 38 del D.Lgs. 163/2006 e s.m.i., e più precisamente:""",'due','tre']
        seconda_lista = [u'di essere cittadino italiano;',u'l’insussistenza dello stato di fallimento, di liquidazione coatta, di concordato preventivo, o l’inesistenza di un procedimento per la dichiarazione di una di tali situazioni;']
        footer = 'Roma'
        footer_destra = 'Firma'
        
        styles=getSampleStyleSheet()
        styles.add(ParagraphStyle(name='titolo', alignment=TA_CENTER , fontSize=14, fontName='Times-Bold'))
        styles.add(ParagraphStyle(name='sottotitolo', alignment=TA_CENTER , fontSize=12, fontName='Times'))
        styles.add(ParagraphStyle(name='destinatario', alignment=TA_RIGHT ,fontName='Times',fontSize=12,))
        styles.add(ParagraphStyle(name='oggetto', alignment=TA_JUSTIFY ,fontName='Times-Bold',fontSize=12,leading = 16))
        styles.add(ParagraphStyle(name='normale', alignment=TA_JUSTIFY ,fontName='Times',fontSize=12,leading = 16))
        styles.add(ParagraphStyle(name='dichiara', alignment=TA_CENTER , fontSize=12, fontName='Times-Bold'))
        styles.add(ParagraphStyle(name='rientro', alignment=TA_JUSTIFY ,fontName='Times',fontSize=12,leading = 16,leftIndent = 20, bulletIndent=5, bulletFontName='Times-Roman' , bulletFontSize=12  ))
        styles.add(ParagraphStyle(name='secondo_rientro', alignment=TA_JUSTIFY ,fontName='Times',fontSize=12,leading = 16,leftIndent = 50, bulletIndent=30, bulletFontName='Times-Roman', bulletFontSize=12 ))
        styles.add(ParagraphStyle(name='footer', alignment=TA_JUSTIFY ,fontName='Times',fontSize=12 , leftIndent = 80))
        styles.add(ParagraphStyle(name='footer_destra', alignment=TA_JUSTIFY ,fontName='Times',fontSize=12 , leftIndent = 380))

        # TITOLO      
        Story.append(Paragraph(titolo, styles["titolo"]))
        Story.append(Spacer(1, 10))
        # SOTT0TITOLO    
        Story.append(Paragraph(sottotitolo, styles["sottotitolo"]))
        Story.append(Spacer(1, 20))
        # INDIRIZZO   
        for elem in indirizzo:
            Story.append(Paragraph(elem, styles["destinatario"]))
            Story.append(Spacer(1, 10))
        Story.append(Spacer(1, 20))
        # OGGETTO DICHIRAZIONE   
        Story.append(Paragraph(oggetto, styles["oggetto"]))
        Story.append(Spacer(1, 20))
        # GARA
        Story.append(Paragraph(gara_testo, styles["normale"]))
        Story.append(Spacer(1, 20))
        # SOGGETTO DICHIARANTE
        Story.append(Paragraph(dichiarazione_soggetto_testo, styles["normale"]))
        Story.append(Spacer(1, 20))
        # PAROLE DICHIARA
        Story.append(Paragraph(dichiara, styles["dichiara"]))
        Story.append(Spacer(1, 20))
        # DICHIARAZIONE
        i = 1
        for elem in primo_elenco:
            Story.append(Paragraph(elem,  styles["rientro"], bulletText=str(i)+')'))
            i = i + 1
            lettera = ord('z')
            for  due in seconda_lista:
                if lettera < 123:
                    Story.append(Paragraph(due,  styles["secondo_rientro"], bulletText=str(chr(lettera))+'.'))
                    Story.append(Spacer(1, 5))
                else:
                    new_letter = lettera-123+97
                    Story.append(Paragraph(due,  styles["secondo_rientro"], bulletText='a'+str(chr(new_letter))+'.'))
                lettera = lettera +1
            Story.append(Spacer(1, 10))
        # FINE DICHIARAZIONE
        # FOOTER         
        Story.append(Paragraph(footer, styles["footer"]))
        Story.append(Paragraph(footer_destra, styles["footer_destra"]))
        
        doc.build(Story)
        pdf = buffer.getvalue()
        buffer.close()
        return pdf
    def generaTabella(self):
        
        buffer = self.buffer
        
        p = canvas.Canvas(buffer)
        
        doc = SimpleDocTemplate(buffer,pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)
        elements = []
        
        indirizzo  = """fsdf
        /n fdsf
        """
        data= [['intestazione', 'intestazione'],
               ['intestazione', 'intestazione'],
               ['intestazione', 'intestazione'],
               ['Indirzzo', 'Indirzzo'],
               ['Indirzzo', 'Indirzzo'],
               [indirizzo, 'Indirzzo']]
        t=Table(data,280, 106)
        t.setStyle(TableStyle([('ALIGN',(0,0),(1,2),'CENTER'),
                               ('TEXTCOLOR',(0,0),(1,2),colors.black),
                               ('VALIGN',(0,0),(1,2),'MIDDLE'),
                               ('ALIGN',(0,3),(-1,-1),'LEFT'),
                               ('TEXTCOLOR',(0,3),(-1,-1),colors.black),
                               ('VALIGN',(0,3),(-1,-1),'MIDDLE'),
                               ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                               ]))
         
        elements.append(t)
        # write the document to disk
        doc.build(elements)
        
        pdf = buffer.getvalue()
        buffer.close()
        return pdf
        
from io import BytesIO
def doc_base(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Documenti.pdf"'
    buffer = BytesIO()
    report = MyPrint(buffer, 'Letter')
    pdf = report.genera_pdf()
    response.write(pdf)
    return response
from io import BytesIO
def tabella(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Documenti.pdf"'
    buffer = BytesIO()
    report = MyPrint(buffer, 'Letter')
    pdf = report.generaTabella()
    response.write(pdf)
    return response


# OPERAZIONI SOGGETTO
def soggetto_new(request):
    if request.method == "POST":
        form = SoggetoForm(request.POST)
        if form.is_valid():
            soggetto = form.save(commit=False)
            soggetto.save()
            return redirect('compilaGare.views.soggetto_detail', pk=soggetto.pk)
    else:
        form = SoggetoForm()
    return render(request, 'compilaGare/soggetto_new.html', {'form': form})

def soggetto_detail(request, pk):
    soggetto = get_object_or_404(Soggetto, pk=pk)
    return render(request, 'compilaGare/soggetto_detail.html', {'soggetto': soggetto})

def soggetto_edit(request, pk):
    soggetto = get_object_or_404(Soggetto, pk=pk)
    if request.method == "POST":
        form = SoggetoForm(request.POST, instance=soggetto)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('compilaGare.views.soggetto_detail', pk=soggetto.pk)
    else:
        form = SoggetoForm(instance=soggetto)
    return render(request, 'compilaGare/soggetto_new.html', {'form': form})

# OPERAZIONI GARA
def gara_new(request):
    if request.method == "POST":
        form = GaraForm(request.POST)
        if form.is_valid():
            gara = form.save(commit=False)
            gara.save()
            return redirect('compilaGare.views.gara_detail', pk=gara.pk)
    else:
        form = GaraForm()
    return render(request, 'compilaGare/gara_new.html', {'form': form})

def gara_detail(request, pk):
    gara = get_object_or_404(Gara, pk=pk)
    return render(request, 'compilaGare/gara_detail.html', {'gara': gara})

def gara_edit(request, pk):
    gara = get_object_or_404(Gara, pk=pk)
    if request.method == "POST":
        form = GaraForm(request.POST, instance=gara)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('compilaGare.views.gara_detail', pk=gara.pk)
    else:
        form = GaraForm(instance=gara)
    return render(request, 'compilaGare/gara_new.html', {'form': form})

# OPERAZIONI IMPRESA
def azienda_new(request):
    if request.method == "POST":
        form = AziendaForm(request.POST)
        if form.is_valid():
            azienda = form.save(commit=False)
            azienda.save()
            return redirect('compilaGare.views.azienda_detail', pk=azienda.pk)
    else:
        form = AziendaForm()
    return render(request, 'compilaGare/azienda_new.html', {'form': form})

def azienda_detail(request, pk):
    azienda = get_object_or_404(Azienda, pk=pk)
    return render(request, 'compilaGare/azienda_detail.html', {'azienda': azienda})

def azienda_edit(request, pk):
    azienda = get_object_or_404(Azienda, pk=pk)
    if request.method == "POST":
        form = AziendaForm(request.POST, instance=azienda)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('compilaGare.views.azienda_detail', pk=azienda.pk)
    else:
        form = AziendaForm(instance=azienda)
    return render(request, 'compilaGare/azienda_new.html', {'form': form})

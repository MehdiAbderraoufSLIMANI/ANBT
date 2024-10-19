from django.shortcuts import  render
from django.http import Http404
from .models import Scanner,Ordinateur,Imprimante,Ecran,Serveur
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect

@permission_required('auth.statistics')
def index(request):
    if request.user.is_authenticated:
        scanner = Scanner.objects.all()
        scanner_count = scanner.count()
        scanner_hors_service = scanner.filter(etat_de_materiel = 'Hors service').count()
        scanner_foncting = scanner.filter(etat_de_materiel = 'fonctionne').count()
        scanner_traitement = scanner.filter(etat_de_materiel = 'Traitement').count()
        
        ordinateur = Ordinateur.objects.all()
        ordinateur_count = ordinateur.count()
        ordinateur_hors_service = ordinateur.filter(etat_de_materiel = 'Hors service').count()
        ordinateur_foncting =  ordinateur.filter(etat_de_materiel = 'fonctionne').count()
        ordinateur_traitement = ordinateur.filter(etat_de_materiel = 'Traitement').count()

        imprimante = Imprimante.objects.all()
        imprimante_count = imprimante.count()
        imprimante_hors_service= imprimante.filter(etat_de_materiel = 'Hors service').count()
        imprimante_foncting = imprimante.filter(etat_de_materiel = 'fonctionne').count()
        imprimante_traitement = imprimante.filter(etat_de_materiel = 'Traitement').count()

        ecran = Ecran.objects.all()
        ecran_count = ecran.count()
        ecran_hors_service = ecran.filter(etat_de_materiel = 'Hors service').count()
        ecran_foncting =  ecran.filter(etat_de_materiel = 'fonctionne').count()
        ecran_traitement =  ecran.filter(etat_de_materiel = 'Traitement').count()
        
        serveur = Serveur.objects.all()
        serveur_count = serveur.count()
        serveur_hors_service = serveur.filter(etat_de_materiel = 'Hors service').count()
        serveur_foncting = serveur.filter(etat_de_materiel = 'fonctionne').count()
        serveur_traitement = serveur.filter(etat_de_materiel = 'Traitement').count()
            
        context = {

            'Scanner': scanner,
            'scanner_count': scanner_count,
            'scanner_hors_service':scanner_hors_service,
            'scanner_foncting':scanner_foncting,
            'scanner_traitement':scanner_traitement,

            'ordinateur': ordinateur,
            'ordinateur_count': ordinateur_count,
            'ordinateur_hors_service':ordinateur_hors_service,
            'ordinateur_foncting':ordinateur_foncting,
            'ordinateur_traitement':ordinateur_traitement,
            
            'imprimante': imprimante,
            'imprimante_count': imprimante_count,
            'imprimante_hors_service':imprimante_hors_service,
            'imprimante_foncting':imprimante_foncting,
            'imprimante_traitement':imprimante_traitement,
            
            'ecran': ecran,
            'ecran_count': ecran_count,
            'ecran_hors_service':ecran_hors_service,
            'ecran_foncting':ecran_foncting,
            'ecran_traitement':ecran_traitement,
            
            'serveur': serveur,
            'serveur_count': serveur_count,
            'serveur_hors_service':serveur_hors_service,
            'serveur_foncting':serveur_foncting,
            'serveur_traitement':serveur_traitement,
                }

        return render(request,'dashboard/index.html',context)
    else:
        return HttpResponseRedirect('admin')

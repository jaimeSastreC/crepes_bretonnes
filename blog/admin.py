from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.utils.text import Truncator
from .models import Categorie, Article, Comment


class ArticleAdmin(admin.ModelAdmin):
   list_display   = ('titre', 'auteur', 'date', 'apercu_contenu')
   list_filter    = ('auteur','categorie',)
   date_hierarchy = 'date'
   ordering       = ('date', )
   search_fields  = ('titre', 'contenu')

   def apercu_contenu(self, article):
      """
      Retourne les 40 premiers caractères du contenu de l'article,
      suivi de points de suspension si le texte est plus long.
      """
      return Truncator(article.contenu).chars(40, truncate='...')


   # En-tête de notre colonne
   apercu_contenu.short_description = 'Aperçu du contenu'

   # champs définis dans le formulaire admin
   # fields = ('titre', 'auteur', 'categorie', 'contenu')

   # préremplis champ slug avec titre, peut être modifié
   prepopulated_fields = {'slug': ('titre',), }

   # fileds plus complexe avec fieldset
   fieldsets = (
      # Fieldset 1 : meta-info (titre, auteur…) // collapse choix visible ou non, tel Togle
      ('Général', {
         'classes': ['collapse', ],
         'fields': ('titre', 'slug', 'auteur', 'categorie')
      }),
      # Fieldset 2 : contenu de l'article
      ('Contenu de l\'article', {
         'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
         'fields': ('contenu',)
      }),
   )


admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
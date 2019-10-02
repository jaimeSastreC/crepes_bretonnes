from django.db import models

# Create your models here.


class Crepe(models.Model):
    crepe_nom = models.CharField(unique=True, max_length=150)
    crepe_prix = models.IntegerField(blank=True, null=True)

class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Categorie d'Article"
        ordering = ['nom'] #pas nécessaire

    def __str__(self):
        """
        Catégorie d'Articles!
        rappel: Clé étrangère dans Article
        """
        return self.nom

class Article(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True)
    auteur = models.CharField(max_length=32)
    contenu = models.TextField(null=True)
    # option: default=timezone.now
    date = models.DateTimeField(auto_now_add=True,
                                auto_now=False,
                                verbose_name="Date de parution")
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    # informations Admin, affichage
    class Meta:
        verbose_name = "article du Blog"
        ordering = ['date']

    def __str__(self):
        """
        Articles à publier, selon Catégorie,
        rappel: clé étrangère vers Categorie
        """
        return self.titre

class Comment(models.Model):
    contenu = models.TextField(null=False)
    auteur = models.CharField(max_length=32)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Commentaire d'article"

    def __str__(self):
        # tuple of reference
        return self.id, self.article


class Contact(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    photo = models.ImageField(upload_to="static/img/")

    def __str__(self):
        return self.nom

########################### one to one ###########################

class Moteur(models.Model):
    nom = models.CharField(max_length=25)

    def __str__(self):
        return self.nom

class Voiture(models.Model):
    nom = models.CharField(max_length=25)
    moteur = models.OneToOneField(Moteur, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

########################### many to many ##########################

class Produit(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

class Vendeur(models.Model):
    nom = models.CharField(max_length=30)
    produits = models.ManyToManyField(Produit, through='Offre',
                                      related_name='+')
    produits_sans_prix = models.ManyToManyField(Produit, related_name="vendeurs")

    def __str__(self):
        return self.nom

class Offre(models.Model):
    prix = models.IntegerField()
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    vendeur = models.ForeignKey(Vendeur, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} vendu par {1}".format(self.produit, self.vendeur)
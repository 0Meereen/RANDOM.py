import discord
import random

client = discord.Client()

@client.command()
async def random_image(ctx):
  # Récupération de la liste des fichiers dans le dossier "images"
  image_list = os.listdir("images")
  
  # Sélection d'une image au hasard à partir de la liste
  random_image = random.choice(image_list)
  
  # Envoi de l'image sélectionnée au channel
  await ctx.send(file=discord.File(random_image))

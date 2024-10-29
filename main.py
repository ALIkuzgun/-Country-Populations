import pygame
import pandas as pd
import os 

country_value = pd.read_csv('population_data.csv', encoding='ISO-8859-1')


pygame.init()

width = 520
height = 440

ekran = pygame.display.set_mode((width, height))
pygame.display.set_caption('Countries Population')
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 54)
font3 = pygame.font.Font(None, 44)

bg = pygame.image.load("back_ground.jpg")

input_text = ""
country_stats = ""
country_stats2 = ""
country_stats3 = ""
country_stats_name = ""

def get_country_stats(name):
    row = country_value[country_value['Country'].str.lower() == name.lower()]
    if not row.empty:
        stats = row.iloc[0]
        return {
            'Country': stats['Country'],
            'Population': stats['Population'],
            'Yearly Change': stats['Yearly Change'],
            'Net Change': stats['Net Change']
        }
    return None

text_title = font2.render("2024 Country Population",True,(0,0,0))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if len(input_text) < 19:
                if event.key == pygame.K_RETURN:
                    stats = get_country_stats(input_text)
                    if stats:
                        country_stats_name = f"Country: {stats['Country']}"
                        country_stats = f"Population: {stats['Population']}"
                        country_stats2 = f"Yearly Change: {stats['Yearly Change']}"
                        country_stats3 = f"Net Change: {stats['Net Change']}"
                    input_text = "" 
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode 

    ekran.fill((255, 0, 0))
    ekran.blit(bg, (-40, -100))
    pygame.draw.rect(ekran, (0, 0, 0), (105, 93, 300, 40), 2)
    pygame.draw.rect(ekran, (255, 255, 255), (107, 95, 296, 36))
    text_input = font.render(input_text, True, (0, 0, 0))
    ekran.blit(text_input, (110, 100))
    ekran.blit(text_title, (28, 20))

    if country_stats:
        text_stats = font3.render(country_stats, True, (0, 0, 0))
        ekran.blit(text_stats, (100, 250))
    if country_stats2:
        text_stats = font3.render(country_stats2, True, (0, 0, 0))
        ekran.blit(text_stats, (100, 300))
    if country_stats_name:
        text_stats = font2.render(country_stats_name, True, (0, 0, 0))
        ekran.blit(text_stats, (110, 180))
    if country_stats3:
        text_stats = font3.render(country_stats3, True, (0, 0, 0))
        ekran.blit(text_stats, (102, 350))

    pygame.display.flip()

pygame.quit()
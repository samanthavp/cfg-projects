# Original code with the basic function of searching recipes from one inputted ingredient

import requests


def recipe_search(ingredient):
    app_id = 'd09719e6'
    app_key = '3a4837a52d4a5061a7de09f9e033938a'
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()

    return data['hits']

def run():
    ingredient = input('Enter an ingredient: ')

    results = recipe_search(ingredient)

    with open('CFG_Team_4_file.txt', 'w', encoding='utf-8') as Team4:
        for result in results:
            recipe = result['recipe']
            list = (recipe['ingredientLines'])
            ingredientlist = '\n'.join(repr(item) for item in list)

            print(recipe['label'])
            print(recipe['url'])
            print("Ingredients: ", '\n', (ingredientlist))
            print(' ')

            Team4.writelines(
                [recipe['label'], '\n', recipe['url'], '\n', "Ingredients: \n", (ingredientlist), '\n', ' \n'])


run()


















# # import requests
# #
# #
# # def recipe_search(ingredient):
# #     app_id = 'd09719e6'
# #     app_key = '3a4837a52d4a5061a7de09f9e033938a'
# #     result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
# #     data = result.json()
# #
# #     return data['hits']
# #
# #
# # def run():
# #     ingredient = input('Enter an ingredient: ')
# #
# #     results = recipe_search(ingredient)
# #
# #     for result in results:
# #         recipe = result['recipe']
# #         print(recipe['label'])
# #         print(recipe['url'])
# #         list = (recipe['ingredientLines'])
# #         ingredientlist = '\n'.join(repr(item) for item in list)
# #         print("Ingredients: ", '\n', (ingredientlist))
# #         print()
# #
# #         Team4 = open('CFG_Team_4_file.txt', 'a')
# #
# #         for i in range(0, 11):
# #             Team4.writelines([recipe['label'], '\n', recipe['url'], '\n', "Ingredients: \n", (ingredientlist), '\n', ' \n'])
# #
# #
# # run()
#
#
#
#
# import tkinter as tk
# from tkinter.font import Font
# from io import BytesIO
# from PIL import Image, ImageTk
# from py_edamam import Edamam
# import requests
#
# # import webbrowser
#
#
# recipe_image_width = ''
# recipe_image_height = ''
#
# # Create Interface/App Structure With Tkinter
# window = tk.Tk()
# window.geometry('')
# window.configure(bg='yellow')
# window_title = 'CFG Team4 Recipe App'
# window.title(window_title)
#
# my_font = Font(
#     family='League Spartan',
#     size=15,
#     weight='normal',
#     slant='roman',
#     underline=False,
#     overstrike=False
# )
#
# frame_a = tk.Frame(master=window, relief=tk.FLAT, borderwidth=5)
# label = tk.Label(master=frame_a, text='Your Dietary Recipes!',
#                  font=my_font, fg='blue', bg='yellow', width=100, height=5)
#
# frame_b = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=5)
# button = tk.Button(master=frame_b, text='Search', font='calligraphy', width=15, height=1, fg='blue', bg='yellow',
#                    command=lambda: run_search_query())
#
# frame_b_label = tk.Label(master=frame_b, text='Enter an Ingredient', font='calligraphy',
#                          width=30, height=1, fg='blue', bg='yellow')
#
# frame_a.pack()
# label.pack(fill=tk.BOTH)
# frame_b.pack(side=tk.TOP, fill=tk.X)
# button.pack_configure(side=tk.RIGHT, padx=5)
# frame_b_label.pack(side=tk.LEFT, padx=5)
#
# entry = tk.Entry(master=frame_b, fg='black', bg='yellow', width=110)
# entry.pack_configure(side=tk.RIGHT, expand=100)
#
# entry.insert(0, 'Enter an ingredient')
# entry.delete(0, tk.END)
#
#
# # Create user functions whose queries can be accessed from 'Search' button when clicked
# def run_search_query():
#     query = entry.get()
#
#     recipe = get_recipe(query)
#
#     # Check and return recipe image
#     #    if recipe:
#     #        image = "https://api.edamam.com/api/recipes/v2/images"
#     #        recipe1 = requests.get(image)
#     #        recipe_image = requests.api
#     #        recipe_url = requests.patch(url="https://api.edamam.com/api/recipes/v2/images")
#     #        return recipe_image, recipe_url
#
#     # Return Error404 Image if recipe is not found
#     #    else:
#     #        recipe_image = 'https://images.app.goo.gl/VARspi4ai9MYqdW28'
#     #        recipe_url = ''
#
#     #        get_image('')
#     get_ingredient(recipe)
#
#
# #        return recipe_image, recipe_url
#
# # Get more information of recipe not included in ingredient search
# #    def open_recipe_link():
# #        webbrowser.open_new_tab(recipe_url)
#
# #        recipe_link_button = tk.Button(master=window, text='Search',
# #                                       highlightbackground='sky blue', command=open_recipe_link)
# #        recipe_link_button.grid(column=1, row=7, pady=10)
#
#
# # Get recipe from ingredient search
# def get_recipe(query, recipe_app_id='d09719e6', recipe_app_key='3a4837a52d4a5061a7de09f9e033938a'):
#     edamame_object = Edamam(recipes_appid=recipe_app_id, recipes_appkey=recipe_app_key)
#     query_result = edamame_object.search_recipe(query)
#
#     for recipe in query_result:
#         return recipe
#
#
# # Get recipe image from ingredient search
# def get_image(image_url=''):
#     response = requests.get(image_url)
#
#     img = Image.open(BytesIO(response.content))
#     #    img = img.resize(recipe_image_height)
#     image = ImageTk.PhotoImage(img)
#
#     holder = tk.Label(master=window, image=image)
#     holder.photo = image
#     holder.pack(anchor="center", side=tk.LEFT)
#
#
# # Get recipe from ingredient search
# def get_ingredient(recipe):
#     ingredients = tk.Text(master=window, height=25, width=50, bg='white')
#     ingredients.pack(anchor="center", side=tk.RIGHT)
#     ingredients.delete('1.0', tk.END)
#
#     if recipe is None:
#         ingredients.insert(tk.END, 'No recipe was found for search criteria')
#         return
#
#     ingredients.insert(tk.END, '\n' + recipe + '\n')
#     for ingredients in recipe:
#         ingredients.insert(tk.END, '\n' + ingredients)
#         return
#
#     results = recipe(ingredients)
#     for result in results:
#         recipe = result['recipe']
#
#         result.insert(tk.END, '\n' + recipe.label + '\n')
#         result.insert(tk.END, '\n' + recipe.ingredientLines)
#         return
#
#
# # Function to run the app
# def run_app():
#     if __name__ == '__main__':
#         app_id = 'd09719e6'
#         app_key = '3a4837a52d4a5061a7de09f9e033938a'
#
#         recipe_app = (app_id, app_key)
#         return recipe_app
#
#
# run_app()
#
# window.mainloop()

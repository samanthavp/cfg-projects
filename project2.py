import requests


def recipe_search(ingredient, excluded):
  app_id = 'd09719e6'
  app_key = '3a4837a52d4a5061a7de09f9e033938a'
  result = requests.get('https://api.edamam.com/search?q={}&excluded={}&app_id={}&app_key={}'.format(ingredient, excluded, app_id, app_key))

  data = result.json()
  return data['hits']


def run():
  ingredient = input('Enter ingredients to search for (separated by a comma): ')
  excluded = input('Enter one ingredient to exclude (optional): ')
  calorie_check = input('Would you also like to search by calories? (yes or no) ')
  if calorie_check == 'yes':
    calorie_search = True
    no_of_calories = input('What is the maximum calories you want to consume (in numbers)? ')
  else:
    calorie_search = False

  results = recipe_search(ingredient, excluded)

  with open('CFG_Team_4_file.txt', 'w', encoding='utf-8') as Team4:
    # The encoding helps keep the encoding consistent between platforms (UTF-8 is the most preferred encoding method for text encoding).
    # "w" used to clear the file before writing in it
    for result in results:
      recipe = result['recipe']
      list = (recipe['ingredientLines']) # ingredientLines calls a list of ingredients
      ingredientlist = '\n'.join(repr(item) for item in list) # convert the list to a string using the repr function and display on separate lines

      #if calories in recipes are less than user upper limit, display recipe info
      if calorie_search == True and recipe['calories'] <= float(no_of_calories):
        print(recipe['label'])
        print(recipe['url'])
        print('Calories: ', recipe['calories'])
        print("Ingredients: ", '\n', (ingredientlist))
        Team4.writelines([recipe['label'], '\n', recipe['url'], '\n', "Calories: ", str(recipe['calories']), '\n', "Ingredients: \n", (ingredientlist),'\n', ' \n'])

      elif calorie_search == False:
        print(recipe['label'])
        print(recipe['url'])
        print("Ingredients: ", '\n', (ingredientlist))
        Team4.writelines([recipe['label'], '\n', recipe['url'], '\n', "Calories: ", str(recipe['calories']), '\n', "Ingredients: \n", (ingredientlist),'\n', ' \n'])
      print(' ')


run()

import psycopg2
from config import database, user, password
from dictionary import initialize_dictionary, matcher, getValue

def connect_to_database(query):
   try:
      connection = psycopg2.connect(database = database, user = user, password = password)
   except Exception as e:
      print(e)
      sys.exit()

   try:
      cursor = connection.cursor()
      cursor.execute(query)
   except Exception as e:
      print(e)
      sys.exit()

   schema_info = []
   for row in cursor:
      for element in row:
         schema_info.append(element)

   connection.close()
   return schema_info

def find_match(schema_info):
   """This function matches the fields returned from connect_to_database() with dictionary keys and returns them as a list of dictionaries"""
   identified_PIIs = initialize_dictionary()

   best_match_dictionary_list = []
   for field in schema_info:
      best_match = matcher(field, identified_PIIs)
      best_match_values = getValue(best_match, identified_PIIs)
      best_match_dictionary = {"field": best_match, "encryption": best_match_values[0], "masking": best_match_values[1]}

      best_match_dictionary_list.append(best_match_dictionary)

   return best_match_dictionary_list


def main():
   query = '''SELECT field_name FROM schema_info;'''
   schema_info = connect_to_database(query)
   print(find_match(schema_info))

if __name__ == "__main__":
   main()


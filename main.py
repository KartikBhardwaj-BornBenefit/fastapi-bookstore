print('----------------------INVOICE-----------------------')

def generate_invoice(*items, **details):
  for key, value in details.items():
    print(f"{key}: {value}")
    for item in items:
      print(f"item: {items}")


generate_invoice( "aalu","pyar",name ="kartik", age=21 , city ="jhajjar" , state = "haryana", )

  
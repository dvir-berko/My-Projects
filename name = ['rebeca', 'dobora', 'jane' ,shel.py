def Prepare_test_girlz_data():
    names = ['rebeca', 'dobora', 'jane', 'shelly']
    hobbies = ('painint', 'cycling', 'farming', 'pottery')
    girlz_data = [{'name': names[i], 'hobby': hobbies[i]} for i in range(len(names))]
    return girlz_data

names = ['rebeca', 'dobora', 'jane', 'shelly']
hobbies = ('painint', 'cycling', 'farming', 'pottery')

def print_girlz_data(girlz_names, girlz_hobbies):
    if len(names) != len(hobbies):
        pass
    
    for girl_id in range(len(names)):
        print(names[girl_id], 'loves', hobbies[girl_id])
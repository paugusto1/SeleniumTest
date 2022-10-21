from booking.booking import Booking

try:
    with Booking(teardown=False) as bot:
        bot.land_first_page()
        #bot.change_currency('BRL')
        bot.search()
        #bot.apply_filtration()
        bot.generateReports()
except Exception as e:
    if 'in PATH' in str(e):
        print("PATH Issue found!")
    else:
        print(e)

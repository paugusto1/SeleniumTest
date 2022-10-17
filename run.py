from booking.booking import Booking

with Booking(teardown=False) as bot:
    bot.land_first_page()
    #bot.change_currency('BRL')
    bot.search()
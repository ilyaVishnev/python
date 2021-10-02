name = input("Put name: ")
second_name = input("Put second_name: ")
birth_year = input("Put birth year: ")
city = input("Put city: ")
e_mail = input("Put e-mail: ")
phone_number = input("Put phone number: ")


def user_to_line(u_name, u_sec, u_year, u_city, u_mail, u_number):
    return f"name :{u_name},second name: {u_sec},birth year: {u_year},city :{u_city},e-mail: {u_mail}," \
           f"phone number: {u_number}"


print(user_to_line(u_name=name, u_sec=second_name, u_year=birth_year, u_city=city, u_mail=e_mail
                   , u_number=phone_number))

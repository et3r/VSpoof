
import sys, math

def help_panel():
    print('\nUsage: ./vspoof.py [-h] [-d DESTINATION_NUMBER] [-f FAKE_NUMBER] [options]\n')

def verify_noise(i):
    if sys.argv[i+1].lower().strip() != "traffic" and sys.argv[i+1].lower().strip() != "night_club" and sys.argv[i+1].lower().strip() != "crowd" and sys.argv[i+1].lower().strip() != "casino" and sys.argv[i+1].lower().strip() != "cell_noise" and sys.argv[i+1].lower().strip() != "airport" and sys.argv[i+1].lower().strip() != "dogs" and sys.argv[i+1].lower().strip() != "police":
        print("\n[x] You must enter a valid background noise. Use the parameter -h to get more help!")
        sys.exit(2)

def verify_modulator(i):
    if sys.argv[i+1].lower().strip() != "woman" and sys.argv[i+1].lower().strip() != "man":
        print("\n[x] You must enter a valid modulator of voice (woman or man).")
        sys.exit(2)

def verify_phone_number(i):
    # verify if the next argument is indeed a telephonic number, it has to be a number and must be 10 digits long
    try:
        # math.isnan return True or False, in this case we are using it to see if we get an exception, so it would not be a number
        math.isnan(int(sys.argv[i+1]))
        # verify if its 10 digits long
        if len(sys.argv[i+1]) != 10:
            print("\n[x] You must enter a valid phone number.")
            sys.exit(2)
    except Exception as e:
        print("\n[x] You must enter a valid phone number.")
        sys.exit(2)

def args():

    num_req_args = 2 # number of required parameters
    counter = 0 # counter of the required parameters
    final_args = [] # the final return of the function
    options_args = [] # these are the not required parameters, but its used to keep the order in the final_args array

    for i in range(0, len(sys.argv)): # aqui en range de 0 a x no se le resta 1 a x porque el start es 0 y el stop es x, entonces va a recorrer de 0 a x-1
        # Required args
        if (sys.argv[i] == "-d" or sys.argv[i] == "-f"):
            counter += 1

        match sys.argv[i]:
            case "-d":
                verify_phone_number(i)
                # The destination number is always gonna be the first in the array and the fake the second
                if len(final_args) != 0: 
                    # swap of values
                    copy_phone = final_args[0]
                    final_args[0] = sys.argv[i+1]
                    final_args.append(copy_phone)
                else:
                    #if the -d parameter is being used first
                    final_args.append(sys.argv[i+1])
            case "-f":
                verify_phone_number(i)
                final_args.append(sys.argv[i+1])
            case "-m":
                if len(final_args) < 2:
                    verify_modulator(i)
                    options_args.append(sys.argv[i+1])
                else:
                    verify_modulator(i)
                    final_args.append(sys.argv[i+1])
            case "-n":
                if len(final_args) > 2:
                    verify_noise(i)
                    options_args.append(sys.argv[i+1]);
                else:
                    verify_noise(i)
                    final_args.append(sys.argv[i+1])
            case "-r":
                if len(final_args) > 2:
                    options_args.append('record')
                else:
                    final_args.append('record')
                
    if counter != num_req_args:
        # if the parameters werent well executed
        help_panel()
        sys.exit(2)

    for i in options_args:
        # put the extra parameters into the final args array
        final_args.append(i)

    return final_args
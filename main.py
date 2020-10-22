import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message


def run_block_a():
    print("Which program in 'Block A: Basics' do you wish to run?")
    print("***********************************")
    print("simple_message or multiline_message")
    response = input()
    if (response == "simple_message"):
        simple_message.run()

    elif (response == "multiline_message"):
        multiline_message.run()


def run():
    is_running = True

    while(is_running):
        print("""
 _   _      _ _       _ _
| | | | ___| | | ___ | | |
| |_| |/ _ \ | |/ _ \| | |
|  _  |  __/ | | (_) |_|_|
|_| |_|\___|_|_|\___/(_|_)""")
        print("\n\nWhat would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if (response == "a"):
            run_block_a()
        elif (response == "q"):
            break
        else:
            print("Invalid option! Please try again.")
run()


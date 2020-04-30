import os
import datetime
import time
import Processor
from judge import Judge


def check_user_exit(user_input):
    if user_input == 'exit()':
        print("\nThanks for using Image Processor!")
        exit(0)


def set_content():
    content_valid = False
    content_type, content = None, None
    while not content_valid:
        content_input = input("\nPlease type in the absolute path of the "
                              "file/directory\nIf you want to select "
                              "multiple files, please add four colons(::::) "
                              "between the file paths.\nDo not choose multiple"
                              " directories or a combination of files and "
                              "directories.\nYou can type in 'exit()' to exit.")
        check_user_exit(content_input)
        content = content_input.split("::::")
        judge = Judge(content)
        content_type, content = judge.judge_content()
        if content_type <= 0:
            print("Wrong value received!\nDetails: {} Please Try again.".format(content))
        else:
            content_valid = True
    return content_type, content


def set_operation():
    valid_operation = False
    operation_input = None
    while not valid_operation:
        operation_input = input("\nPlease type in the sum of the operation(s) "
                                "you want to apply on the files. "
                                "4 for resize, 2 for rotate, and 1 for "
                                "type_convert.\nFor example, if you only "
                                "want to resize your images, type in 4. "
                                "And if you want to rotate and convert type "
                                "for your images, type in 3.\n"
                                "You can also type in 'exit()' to exit.")
        check_user_exit(operation_input)
        try:
            if int(operation_input) not in range(1, 8):
                print("Wrong values received! Please try again.")
                continue
        except ValueError:
            print("Wrong values received! Please type in INTEGERS "
                  "between 1 and 7 only.")
            continue
        valid_operation = True
    return int(operation_input)


def set_operation_para(operation_para, operation_value):
    if operation_value == 0:
        print("No operation instructions received. ")
        exit(0)
    operation = operation_value
    if operation >= 4:
        operation_para["resize"] = set_resize_para()
        operation -= 4
    if operation >= 2:
        operation_para["rotate"] = set_rotate_para()
        operation -= 2
    if operation >= 1:
        operation_para["type"] = set_convert_para()
        operation -= 1
    assert operation == 0, "Final operation value should be 0.\n\t" \
                           "Final operation value: {}\n\tOriginal " \
                           "input value: {}".format(operation, operation_value)
    return operation_para


def set_resize_para():
    valid_resize = False
    width, height = None, None
    while not valid_resize:
        resize_input = input("\nPlease type in the size of the image(s) after "
                             "processing.\nFor example, if you want your image "
                             "to be of size 600x400, type in 600,400\n"
                             "You can also type in 'exit()' to exit.")
        check_user_exit(resize_input)
        resize_para = resize_input.split(",")
        if len(resize_para) != 2:
            print("Wrong value received! Please try again.\n")
            continue
        else:
            try:
                width, height = int(resize_para[0].strip()), int(resize_para[1].strip())
                if width <= 0 or height <= 0:
                    print("Both values must be INTEGERS that's greater than 0! "
                          "Please try again.")
                    continue
            except ValueError:
                print("Wrong value received. Please make sure the input format"
                      " is correct.")
                continue
        valid_resize = True
    return width, height


def set_rotate_para():
    valid_rotate = False
    while not valid_rotate:
        rotate_input = input("\nPlease type in to what angle you want to rotate "
                             "your image clockwise.\nFor example, type in 180 "
                             "if you want to rotate your image upside down.\n"
                             "You can also type in 'exit()' to exit.")
        check_user_exit(rotate_input)
        try:
            rotate = int(rotate_input)
            rotate = 360 - rotate % 360
            return rotate
        except ValueError:
            print("Wrong value received! Please try again.")


def set_convert_para():
    valid_type = False
    img_type = None
    support_list = ("jpg", "jpeg", "png", "tiff", "gif", "bmp", "pdf", "raw")
    while not valid_type:
        type_input = input("\nPlease type in the type of the image file after "
                           "processing (case insensitive).\nSupported image "
                           "types:\n\t.jpg\t.jpeg\t.png\t.tiff"
                           "\n\t.gif\t.bmp\t.pdf\t.raw\n"
                           "You can also type in 'exit()' to exit.")
        check_user_exit(type_input)
        img_type = type_input.strip(".").lower()
        if img_type not in support_list:
            print("Wrong value received! Please check if the type is supported.")
        else:
            valid_type = True
    return img_type


def set_output_path():
    valid_output = False
    output_path = None
    while not valid_output:
        input_output_path = input("\nPlease set the valid output path.\nExamples:\n"
                                  "\tWindows: to store the processed files in C:\\"
                                  "new_images\, type in C:/new_images/\n\tMacOS: to "
                                  "store the processed files in /home/new_images/, "
                                  "type in /Users/[Your_User_Name]/new_images/\n\t"
                                  "Linux: to store the processed files in /home/"
                                  "new_images/, type in /usr/[Your_User_Name]/"
                                  "new_images/\nYou can also type in 'exit()' to exit.")
        output_original = input_output_path
        check_user_exit(output_original)
        if not os.path.isdir(output_original):
            print('Received: {}' + output_original)
            print("Wrong path received! Please make sure the directory exists.")
        else:
            valid_output = True
            if not output_original.endswith(os.sep):
                output_original += os.sep
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            output_path = output_original + "processed_images_" + \
                timestamp + os.sep
            try:
                os.mkdir(output_path)
            except FileExistsError:
                time.sleep(1)
    return output_path


def run_program():
    log_path = "/Users/zhangmengfeifei/Desktop/self_learning/test_files/log.txt"
    parameters = dict()
    print("Welcome to Image Process Master!")
    parameters["content_type"], parameters["content"] = set_content()
    operation = set_operation()
    set_operation_para(parameters, operation)
    output_path = set_output_path()
    processor = Processor.Processor(parameters, output_path, log_path)
    # processor.__test_parameters__()
    processor.process()


if __name__ == '__main__':
    pass

import os
from datetime import datetime
from PIL import Image
import judge


class Processor:
    """
    Class Processor is used to create a Processor instance to process image files.
    attributes:
        content: the directory/file(s) to be operated.
        operation: the operation to be applied on the content. The value is the sum of
                   the single operations.
            0: default
            4: resize
            2: rotate
            1: convert file type
        log_file_path: the path of the log file.
    """
    def __init__(self, parameters, output_path, log_path):
        self.parameters = parameters
        content = self.parameters["content"]
        self.judge = judge.Judge(content)
        self.output_path = output_path
        self.log_file_path = log_path
        self.fail_files = []

    def __set_log_file__(self, log_path):
        self.log_file_path = log_path

    def set_output_file(self, original_filename):
        # Sets the output file path for a single file
        # The original filename must be the file name with directory values
        parent_path, suffix = \
            self.output_path, "." + self.parameters["type"]
        last_slash_pos = original_filename.rindex("/")

        # In case the suffix is omitted
        try:
            last_dot_pos = original_filename.rindex(".")
            new_file_name = \
                original_filename[(last_slash_pos + 1):last_dot_pos] + suffix
        except ValueError:
            new_file_name = original_filename[(last_slash_pos + 1):] + suffix

        new_file_path = parent_path + new_file_name
        return new_file_path

    def write_log(self, log_content, time=True, indent=""):
        try:
            with open(self.log_file_path, 'a', encoding='utf-8') as log_file:
                if time:
                    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    if log_content.strip() != "":
                        log_file.write("{}{} {}\n".format(indent, time, log_content))
                else:
                    log_file.write("{}{}\n".format(indent, log_content))

        except:
            print("Fatal! Can't log errors")

    def __test_parameters__(self):
        # This is a function for test use.
        list_para = dict()
        list_para["parameters"] = self.parameters
        list_para["output_path"] = self.output_path
        list_para["log_path"] = self.log_file_path
        print(list_para)

    def return_PIL_image(self, image):
        # This function is used to check if the parameter is an instance of
        # PIL.Image.Image. If not, convert it to.
        if not isinstance(image, Image.Image):
            return Image.open(image)
        return image

    def convert_rgb(self, original_filename):
        # Convert a PIL.Image.Image instance to RGB format.
        new_image = self.return_PIL_image(original_filename).convert("RGB")
        return new_image

    def resize(self, original_filename, new_size):
        # Resize a PIL.Image.Image instance.
        new_image = self.return_PIL_image(original_filename).resize(new_size)
        return new_image

    def rotate(self, original_filename, counter_clockwise_rotate_angle):
        # Rotate a PIL.Image.Image instance.
        new_image = self.return_PIL_image(original_filename).rotate(counter_clockwise_rotate_angle)
        return new_image

    def process_single_file(self, original_filename):
        # This function is used to process a single image file.
        # The parameter "original_filename" must be the absolute file path.
        new_image = None
        flag = ""  # Success flag
        operations = dict()
        operations["resize_to"] = self.parameters.get("resize", "N/A")
        operations["rotate"] = self.parameters.get("rotate", "N/A")
        operations["change_type_to"] = self.parameters.get("type", "N/A")
        output_file_path = self.set_output_file(original_filename)

        try:
            # Convert image file to RGB-formatted
            new_image = self.convert_rgb(original_filename)
            if "resize" in self.parameters:
                new_image = self.resize(new_image, self.parameters["resize"])
            if "rotate" in self.parameters:
                new_image = self.rotate(new_image, self.parameters["rotate"])

            if "type" in self.parameters:
                new_type = self.parameters["type"]
                new_image.save(output_file_path, new_type)
            else:
                new_image.save(output_file_path)

            flag = "SUCCESS: Single-File"
            return 1
        except:
            flag = "FAIL: Single-File"
            self.fail_files.append(original_filename)
            return 0
        finally:
            # Log the processed file
            log_content = "{}: Original file: {} New file: {} Operations: {}" \
                .format(flag, original_filename, output_file_path, operations)
            # print(log_content)
            log_flag = flag + ":"
            log_original_file = "Original file: {}".format(original_filename)
            log_output_file_path = "New File: {}".format(output_file_path)
            log_operations = "Operations: {}".format(operations)
            self.write_log(log_flag, time=False, indent="  ")
            self.write_log(log_original_file, time=False, indent="    ")
            self.write_log(log_output_file_path, time=False, indent="    ")
            self.write_log(log_operations + "\n", time=False, indent="    ")

    def process(self):
        total_count = 0
        success_count = 0
        self.write_log(")\n", indent=("-" * 120 + "\n\nSTART NEW PROCESS: ( Start-time: "))
        summary = "SUMMARY: "

        # Single image file
        if self.parameters["content_type"] == 1:
            total_count = 1
            original_file = self.parameters["content"]
            if_success = self.process_single_file(original_file)
            success_count += if_success

        # Single directory
        elif self.parameters["content_type"] == 2:
            parent_path = self.parameters["content"]
            original_files = sorted(os.listdir(parent_path))
            for original_file in original_files:
                if_success = self.process_single_file(parent_path + original_file)
                success_count += if_success
                total_count += 1

        # Multiple image files
        elif self.parameters["content_type"] == 3:
            original_files = self.parameters["content"]
            for original_file in original_files:
                if_success = self.process_single_file(original_file)
                success_count += if_success
                total_count += 1

        else:
            error = "***FATAL ERROR: Unknown type of processing content. Parameters: {} "\
                .format(self.parameters)
            print(error)
            self.write_log("***\n", indent=error)

        # If no success files, delete new directory
        if success_count == 0:
            os.rmdir(self.output_path)

        summary += "Processed {} file(s) in total. Success files: {} " \
            .format(total_count, success_count)
        print(summary)
        if len(self.fail_files) != 0:
            print("Failed files: ")
            for file in self.fail_files:
                print(file)

        if len(self.fail_files) == 0:
            self.write_log("\n\n" + "-" * 120, indent=(summary + "Finish time: "))
        else:
            self.write_log("Failed files: ", indent=(summary + "Finish time: "))
            self.write_log("\n\n" + "-" * 120, time=False,
                           indent="{}".format(self.fail_files))


if __name__ == '__main__':
    pass

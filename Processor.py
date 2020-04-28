import datetime
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

    def __set_log_file__(self, log_path):
        self.log_file_path = log_path

    def set_output_file(self, original_path):
        pass
        #TODO
        # if dir, make new dir in the current env
        # if multi files, make new dir in the current env
        # if single file, make new file in the current env

    def write_log(self, log_content):
        try:
            with open(self.log_file_path, 'a', encoding='utf-8') as log_file:
                time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if log_content.strip() != "":
                    log_file.write("{} {}\n".format(time, log_content))
        except:
            print("Fatal! Can't log errors")

    def __test_parameters__(self):
        list_para = dict()
        list_para["parameters"] = self.parameters
        list_para["output_path"] = self.output_path
        list_para["log_path"] = self.log_file_path
        print(list_para)

    def convert_rgb(self):
        pass

    def resize(self):
        pass

    def rotate(self):
        pass

    def convert_type(self):
        pass

    def process(self):

            #set output
            #convert("RGB")
            #TODO: process files
            success_info = "Process finished successfully"
            print(success_info)
            self.write_log("{}\n".format(success_info))


if __name__ == '__main__':

    path = "/Users/zhangmengfeifei/Desktop/self_learning/test_files/log.txt"
    for l in list:
        processor = Processor(l, path)
        processor.process()



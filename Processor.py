import datetime
import judge


class Processor:
    """
    Class Processor is used to create a Processor instance to process image files.
    """
    def __init__(self, content, log_path):
        self.content = content
        self.log_file_path = log_path
        self.judge = judge.Judge(content)

    def __set_log_file__(self, log_path):
        self.log_file_path = log_path

    def write_log(self, content):
        try:
            with open(self.log_file_path, 'a', encoding='utf-8') as log_file:
                time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if content.strip() != "":
                    log_file.write("{} {}\n".format(time, content))
        except:
            print("Fatal! Can't log errors")

    def process(self):
        judge_result, judge_error = self.judge.judge_content()
        if judge_result >= 900:
            # means we have an error when judging, and we need to log the error
            self.write_log(judge_error + "\n")
        else:
            self.write_log("Process finished successfully!\n")


if __name__ == '__main__':
    file1 = "/Users/zhangmengfeifei/Desktop/self_learning/test_files/log.txt"
    file2 = "/Users/zhangmengfeifei/Desktop/self_learning"
    file3 = "/Users/zhangmengfeifei/Desktop1/"
    file4 = "/Users/zhangmengfeifei/Desktop/Good afternoon everyone.docx"
    file5 = "/Users/zhangmengfeifei/Desktop/Good afternoon everyone.docx/"
    list = []
    list.append(file1)
    list.append(file2)
    list.append(file3)
    list.append(file4)
    list.append(file5)
    path = "/Users/zhangmengfeifei/Desktop/self_learning/test_files/log.txt"
    processor = Processor(list, path)
    processor.process()



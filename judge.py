import os
import PIL
from PIL import Image


class Judge:
    """
    Class Judge is used to create a Judge instance to judge
     the type of parameters before processing image files
    """
    def __init__(self, content):
        self.content_to_judge = content
        self.value = dict()

    def judge_single_content(self):
        """
            This function is to judge if the content parameter is a directory or a file
            :return values: -1: file Not Found
                            1: single file that could possibly be processed
                            2: single directory
                            0: single file that can't be processed
        """
        if not os.path.exists(self.content_to_judge):
            content_type = -1
            content = "ERROR! File doesn't exist: {}".format(self.content_to_judge)
        else:
            if os.path.isfile(self.content_to_judge):
                try:
                    Image.open(self.content_to_judge)
                except PIL.UnidentifiedImageError:
                    content_type = 0
                    content = "ERROR! {} is not an Image file.".format(self.content_to_judge)
                    return  content_type, content
                content_type = 1
                content = self.content_to_judge
            elif os.path.isdir(self.content_to_judge):
                content_type = 2
                content = self.content_to_judge
            else:
                content_type = 0
                content = "ERROR! Unknown type of file: {} ".format(self.content_to_judge)
        return content_type, content

    def judge_content(self):
        """
        This function is to judge if the content parameter is a directory, a file, or a group of files
        :return values: -1: file Not Found
                        0: single file that can't be processed
                        1: single file that could possibly be processed
                        2: single directory
                        3: multiple files that could possibly be processed
                        -3: a combination of directories or a combination of files and directories
                        -2: other
        """
        if isinstance(self.content_to_judge, str):
            # Single file or directory
            content_type, content = self.judge_single_content()
        elif isinstance(self.content_to_judge, list) and len(self.content_to_judge) == 1:
            self.content_to_judge = self.content_to_judge[0]
            content_type, content = self.judge_single_content()
        elif isinstance(self.content_to_judge, list):
            # Multiple files
            content_list = self.content_to_judge
            for item in self.content_to_judge:
                self.content_to_judge = item
                content_type, content = self.judge_single_content()
                if content_type <= 0:
                    return content_type, content
                if content_type == 2:
                    content = "ERROR! Please do not choose multiple directories or " \
                              "a combination of files and directories."
                    return -3, content
            content_type = 3
            content = content_list
        else:
            # Error
            content_type = -2
            content = "ERROR when running 'judge_content': " \
                      "unknown type of content: {}, error code = {}"\
                      .format(self.content_to_judge, content_type)
        return content_type, content


if __name__ == '__main__':
    path = "/Users/zhangmengfeifei/Desktop/self_learning/test_files/"

    ls = []
    file1 = "/Users/zhangmengfeifei/Desktop/self_learning/test_files/log.txt"
    ls.append(file1)
    file2 = "/Users/zhangmengfeifei/Desktop/self_learning"
    ls.append(file2)
    # file3 = "/Users/zhangmengfeifei/Desktop1/"
    # ls.append(file3)
    file4 = "/Users/zhangmengfeifei/Desktop/Good afternoon everyone.docx"
    ls.append(file4)
    # file5 = "/Users/zhangmengfeifei/Desktop/Good afternoon everyone.docx/"
    # ls.append(file5)

    # for l in ls:
    #     judger = Judge(l)
    #     # print(judger.judge_content())
    # judger = Judge(ls)
    # print(judger.judge_content())
    im = Image.open(file1)

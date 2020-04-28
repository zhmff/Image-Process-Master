import os


class Judge:
    """
    Class Judge is used to create a Judge instance to judge
     the type of parameters before processing image files
    """
    def __init__(self, content):
        self.content_to_judge = content

    def judge_single_content(self):
        """
            This function is to judge if the content parameter is a directory or a file
            :return values: 900: file Not Found
                            1: single file that could possibly be processed
                            2: single directory
                            901: single file that can't be processed
        """
        error_content = ''
        if not os.path.exists(self.content_to_judge):
            return_type = 900
            error_content = "ERROR when running 'judge_single_content': " + \
                            "file doesn't exist: {}, error code = {}"\
                                .format(self.content_to_judge, return_type)
        else:
            if os.path.isfile(self.content_to_judge):
                return_type = 1
            elif os.path.isdir(self.content_to_judge):
                return_type = 2
            else:
                return_type = 901
                error_content = "ERROR when running 'judge_single_content': " \
                                "unknown type of file: {}, error code = {}"\
                                    .format(self.content_to_judge, return_type)
        return return_type, error_content

    def judge_content(self):
        """
        This function is to judge if the content parameter is a directory, a file, or a group of files
        :return values: 900: file Not Found
                        1: single file that could possibly be processed
                        2: single directory
                        901: single file that can't be processed
                        3: multiple files that could possibly be processed
                        910: other
        """
        error_content = ""
        if type(self.content_to_judge) == type(""):
            # Single file
            return_type, error_content = self.judge_single_content()
        elif type(self.content_to_judge) == type([]):
            # Multiple files
            return_type = 3
        else:
            # Error
            return_type = 910
            error_content = "ERROR when running 'judge_content': " \
                            "unknown type of content: {}, error code = {}"\
                                .format(self.content_to_judge, return_type)
        return return_type, error_content


if __name__ == '__main__':

    pass


import shutil

shutil.copy("phone.txt", "temp.txt")
shutil.move("temp.txt", "temp2.txt")
shutil.copytree("d:\\python_exam", "d:\\new_python_exam")
shutil.rmtree("d:\\new_python_exam")
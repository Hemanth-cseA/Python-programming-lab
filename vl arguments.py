#variable-length arguments
def func(name,*fav_subjects):
  print("\n",name,"likes to read")
  for subject in fav_subjects:
    print(subject)
func("ganesh","maths","programming")
func("Hemanth","c","science","c++")
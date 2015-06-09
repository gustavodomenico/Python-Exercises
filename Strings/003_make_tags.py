# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. 
# In this example, the "i" tag makes <i> and </i> which surround the word "Yay". 
#Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>". 

def make_tags(tag, word):
	return "<%s>%s</%s>" % (tag, word, tag)

assert make_tags('i', 'Yay') == '<i>Yay</i>'
assert make_tags('i', 'Hello') == '<i>Hello</i>'
assert make_tags('cite', 'Yay') == '<cite>Yay</cite>'
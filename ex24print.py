print " Let's practise everything."
print 'you\'d need to know \'but escapes with \\ that do \n newlines and \t tabs.'


poem = """\t The lovely world 
with logic  so firmed  planted
cannot  discern \n the needs of love
nor comprehend passion from intution 
and recquires an explaination
\n\twhere there is more
"""
print "------------------------"
print poem
print "---------------------------------"
five = 10-2+3-6
print "this five is : %s " %five
def secret_formula(started ):
	jelly_beans=started*500
	jars = jelly_beans/1000
	crates = jars/1000
	return jelly_beans,jars,crates
start_point = 1000
beans, jars, crates = secret_formula(start_point)
print "With the starting point od %d:" %start_point
print "we'd have %dbeans, %d jars and %d  crates" %(beans, jars,crates)

start_point = start_point/10

print "We can  also do that this way:"
print "we'd have  %d beans , %d jars, %d crates."%secret_formula(start_point)	

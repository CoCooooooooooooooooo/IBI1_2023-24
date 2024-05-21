import matplotlib.pyplot as plt
import datetime

# count the namber of ontology by DOM
import xml.dom.minidom as minidom
def count_go_terms_by_ontology(xml_file):
    dom = minidom.parse(xml_file)
    terms_count = {
        'molecular_function': 0,
        'biological_process': 0,
        'cellular_component': 0
    }
    
    for term in dom.getElementsByTagName('term'):
        
        namespace = term.getElementsByTagName('namespace')[0].firstChild.nodeValue
        
        if namespace in terms_count:
            terms_count[namespace] += 1
    
    return terms_count

xml_file_path = 'go_obo.xml'
counts = count_go_terms_by_ontology(xml_file_path)

# DOM API time
def count_go_terms_by_dom(xml_file):
    start_time = datetime.datetime.now()  
    dom = minidom.parse(xml_file)
    terms_count = {
        'biological_process': 0,
        'molecular_function': 0,
        'cellular_component': 0
    }
    
    for term in dom.getElementsByTagName('term'):
        namespace = term.getElementsByTagName('namespace')[0].firstChild.nodeValue
        if namespace in terms_count:
            terms_count[namespace] += 1
    
    end_time = datetime.datetime.now()  
    return terms_count, end_time - start_time

# measure and record the time
xml_file_path = 'go_obo.xml'
dom_counts, dom_duration = count_go_terms_by_dom(xml_file_path)

# Using SAX
import xml.sax

class goHandler(xml.sax.ContentHandler):
    # Define a class goHandler, inheriting from xml.sax.ContentHandler
    def __init__(self):
        self.namespace = ""
        self.current_data = ""
        self.current_element = ""
        self.namespace_counts = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
        # Create a dictionary to store the counts

    def startElement(self, tag, attrs):
        self.current_element = tag

    def characters(self, content):
        if self.current_element == 'namespace':
            self.namespace += content.strip()

    def endElement(self, tag):
        if tag == 'namespace' and self.namespace in self.namespace_counts.keys():
        # namespace is an end tag in case of several namespaces in one term
            self.namespace_counts[self.namespace] = self.namespace_counts.get(self.namespace, 0) + 1
            self.namespace = ""
            # Reset namespace
        elif tag == 'term':
            self.current_element = ""
        # If tag is term, the element should be reset

    
    # Adjusted endElement method to ensure 'namespace' is a valid key
    def endElement(self, tag):
        if tag == 'namespace' and self.namespace in self.namespace_counts:
            self.namespace_counts[self.namespace] += 1
            self.namespace = ""  # Reset namespace
        elif tag == 'term':
            self.current_element = ""

# Record the start time
start_time2 = datetime.datetime.now()

parser = xml.sax.make_parser()
# Created an SAX parser instance
handler = goHandler()
# Create a goHandler instance
parser.setContentHandler(handler)  
parser.parse("go_obo.xml")
# Begin parsing the xml file

# Record the end time
end_time2 = datetime.datetime.now()
used_time2 = end_time2 - start_time2

# Print the results in a consistent format
print("Counts by Ontology (SAX):", handler.namespace_counts)
print("Counts by Ontology (DOM):", counts)

# ooutput the result
print('The time taken by SAX is ', used_time2)
print("The time taken by DOM is:", dom_duration)

# compare the time spent by each tool
if used_time2 < dom_duration:
    print("// The quickest was: SAX")
else:
    print("// The quickest was: DOM")

# rename the statistical results of 2 methods
counts_sax = handler.namespace_counts
counts_dom = counts
# define the range and label of bar chart
ontologies = ['biological_process', 'molecular_function', 'cellular_component']
bar_width = 0.35
index = range(len(ontologies))  # Create a range object

# draw the 2 bar charts which are displayed side by side by setting the position offset
plt.bar(index, [counts_sax[o] for o in ontologies], bar_width, label='SAX')
plt.bar([i + bar_width for i in index], [counts_dom[o] for o in ontologies], bar_width, label='DOM')

# Converts the range object to a list and performs the addition operation
plt.xticks([i + bar_width / 2.0 for i in index], ontologies) 

# add legends and labels
plt.xlabel('Ontology')
plt.ylabel('Counts')
plt.title('Counts by Ontology (SAX vs DOM)')
plt.legend()

# show the graph
plt.tight_layout()
plt.show()



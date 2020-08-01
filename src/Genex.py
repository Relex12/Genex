def lexer(file):
    liste = []
    for line in file:
        liste.append(line.split(' '))
    for definition in liste: # removes the '\n' at the end of the last word
        definition.append(definition[-1][:len(definition[-1])-1])
        definition.remove(definition[-2])
    return liste

def display_lex(liste):
    print (liste)
    print ('\n')
    for line in liste:
        print (line)

def dependancy(liste):
    print ("Warning : the input file hasn't been checked")
    graph = {}
    for line in liste:
        graph[line[0]] = []
        for word in line[1:]:
            if not(word in ['>', '|', '(', ')']):
#                print (word)
                graph[line[0]].append(word)
    return graph


# def display_graph(graph):
#     print ("Vide")

if __name__ == '__main__':
    file = open ("tests/test.gram", 'r')
    liste = lexer(file)
    display_lex(liste)
    dependancy(liste)

from xml.etree import ElementTree

OK = True
main_pid = 10000
loop_depth = 0


def compare_xml(left, right, key_info='.'):
    global loop_depth
    loop_depth += 1
    if loop_depth == 1:
        print()
    if left.tag != right.tag:
        print_diff(main_pid, key_info, 'difftag', left.tag, right.tag)
        return
    if left.text != right.text:
        print_diff(main_pid, key_info, 'difftext', left.text, right.text)
        return
    leftitems = dict(left.items())
    rightitems = dict(right.items())
    for k, v in leftitems.items():
        if k not in rightitems:
            s = '%s/%s' % (key_info, left.tag)
            print_diff(main_pid, s, 'lostattr', k, "")
    for k, v in rightitems.items():
        if k not in leftitems:
            s = '%s/%s' % (key_info, right.tag)
            print_diff(main_pid, s, 'extraattr', "", k)
    leftnodes = left.getchildren()
    rightnodes = right.getchildren()
    leftlen = len(leftnodes)
    rightlen = len(rightnodes)
    if leftlen != rightlen:
        s = '%s/%s' % (key_info, right.tag)
        print_diff(main_pid, s, 'difflen', leftlen, rightlen)
        return
    l = leftlen < rightlen and leftlen or rightlen
    d = {}
    for i in range(l):
        node = leftnodes[i]
        if node.tag not in d:
            d[node.tag] = 1
            tag = node.tag
        else:
            tag = node.tag + str(d[node.tag])
            d[node.tag] += 1
        s = '%s/%s' % (key_info, tag)
        compare_xml(leftnodes[i], rightnodes[i], s)


def print_diff(main_pid, key_info, msg, base_type, test_type):
    global OK
    info = u'[ %-5s ] %s -> %-40s [ %s != %s ]' % (msg.upper(), main_pid, key_info.strip('./'), base_type, test_type)
    print()
    info.encode('gbk')
    OK = False


if __name__ == '__main__':
    s1 = '''''<?xml version="1.0" encoding="UTF-8"?> \
     <employees> \ 
     <employee id = '1'> \ 
      <name>linux</name>\ 
      <age>30</age>\ 
     </employee>\ 
     <employee id = '2'> \ 
      <name>windows</name>\ 
      <age>20</age>\ 
     </employee>\ 
     </employees>'''
    s2 = '''''<?xml version="1.0" encoding="UTF-8"?> \
     <employees> \ 
     <employee id = '3'> \ 
      <name>windows</name>\ 
      <age>20</age>\ 
     </employee>\ 
     <employee id = '4'> \ 
      <name>linux</name>\ 
      <age>30</age>\ 
     </employee>\ 
     </employees>'''
    lroot = ElementTree.fromstring(s1)
    rroot = ElementTree.fromstring(s2)
    compare_xml(lroot, rroot)

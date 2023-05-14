""" Data Structures and Algorithms for CL 3, Assignment 4
Course:      Data Structures and Algorithms for Computational Linguistics 3 WS22/23
Author:      Pun Ching Nei
Honor Code:  I pledge that this program represents my work.
I received help from: no one in designing and debugging my program.
"""

import collections


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


    def get_depth(self, node):
        """
        Ex. 4.1
        Get the depth of a Node object with respect to self (the root). You may use == to test for Node equality
        As long as we can run the tests without modification, you may add default parameters to the method if you find
        it useful.
        Return the depth of the Node object if it is found. If the node is not in the subtree, return None.
        Parameters
        ____
        node: the Node object whose depth we are calculating
        """
        count = 0
        queue = collections.deque()
        total = []
        currList = []
        queue.append(self)
        while queue:
            currLength = len(queue)
            while currLength > 0:
                current = queue.popleft()
                currList.append(current)
                currLength -= 1
                if self.left == node or self.right == node:
                    count = 1
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            total.append(currList)
            if node not in currList:
                count = count + 1
        for i in total:
            if node not in i:
                count = None
        return count

    def get_span(self):
        """
        Ex. 4.2
        Complete this function. Note that it is used in the helper method "make_roof" provided below.
        Returns the span of a node. We call "span" the data of all of the descendant leaves of a node. Write it from
        left to right and separated by a single whitespace.
        """
        stack = [self]
        string = ""
        if self.is_leaf():
            string += str(self.data) + " "
        else:
            while len(stack) > 0:
                current = stack.pop()
                if current.right is not None:
                    stack.append(current.right)
                if current.left is not None:
                    stack.append(current.left)
                if current.left is None and current.right is None:
                    string += str(current.data) + " "
        return string

    def to_qtree(self, string="", stack=[], depth=0):
        """
        Ex. 4.3
        Write a Qtree representation of self and its descendants. If a node with descendants has depth greater or equal
        to 3, use a roof below it UNLESS its children are leaves. Please refer to the example in the README.md file.
        Also note the helper methods below.
        You can find the Qtree documentation under the URL https://www.ling.upenn.edu/advice/latex/qtree/qtreenotes.pdf.
        You only need to understand sections 3.1, 3.2 and 3.3. For testing purposes, please always write the label after
        both the left and the right square bracket of the node as explained in section 3.2.
        You can visualize your tree using LaTeX. You may add default parameters to the signature if you find it useful
        and it does not require modifying the tests in any way.
        """
        if string == "":
            string += "\\Tree"

        if not self.is_leaf():
            if depth == 3:
                if self.data == "AdvP" or self.data == "AdjP":
                    string += " " + self.make_roof().strip()
                else:
                    string += " [." + self.data
                    temp = " ]." + self.data
                    stack.append(temp)
                    if self.left is not None:
                        string = self.left.to_qtree(string, stack, depth)
                    string += stack.pop()
            else:
                string += " [." + self.data
                temp = " ]." + self.data
                stack.append(temp)
                if self.left is not None:
                    depth += 1
                    string = self.left.to_qtree(string, stack, depth)
                if self.right is not None:
                    string = self.right.to_qtree(string, stack, depth)
                string += stack.pop()
        else:
            string += "  " + self.data

        return string

    # Helper method for to_qtree(): write the roof over the span of Node. You are NOT allowed to change this
    def make_roof(self):
        roof = "\\qroof{" + self.get_span().strip() + "}"
        roof += "." + str(self.data) + " "
        return roof

    # Helper method to determine if Node is a leaf. You are NOT allowed to change this
    def is_leaf(self):
        return self.right is None and self.left is None

if __name__ == '__main__':
    the = Node("the")
    very = Node("very")
    big = Node("big")
    dog = Node("dog")
    slept = Node("slept")
    quite = Node("quite")
    peacefully = Node("peacefully")
    adv1 = Node("Adv", very)
    advP1 = Node("AdvP", adv1)
    adj = Node("Adj", big)
    adjP = Node("AdjP", advP1, adj)
    n = Node("N", dog)
    np2 = Node("NP", adjP, n)
    det = Node("Det", the)
    np1 = Node("NP", det, np2)
    v = Node("V", slept)
    adv2 = Node("Adv", quite)
    advP2 = Node("AdvP", adv2)
    adv3 = Node("Adv", peacefully)
    advP3 = Node("AdvP", advP2, adv3)
    vp = Node("VP", v, advP3)
    s = Node("S", np1, vp)

    s.to_qtree()
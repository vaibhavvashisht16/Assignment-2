{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "acd7ad8a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Print the first side of the triangle:3\n",
      "Print the second side of the triangle:4\n",
      "Print the third side of the triangle:3\n",
      "The Triangle is: Isosceles\n"
     ]
    }
   ],
   "source": [
    "def classify_triangle(x=0, y=0, z=0):\n",
    "    c=max(x,y,z)\n",
    "    a=min(x,y,z)\n",
    "    b=(x+y+z)-a-c\n",
    "    if (a+b <= c) or (b+c <= a) or (a+c <= b):\n",
    "        return \"Not a Triangle\"\n",
    "    elif a == b == c:\n",
    "        return \"Equilateral\"\n",
    "    elif a == b or b == c:\n",
    "        return \"Isosceles\"\n",
    "    elif a ** 2 + b ** 2 == c ** 2:\n",
    "        return \"Right\"\n",
    "    else:\n",
    "        return \"Scalene\"\n",
    "\n",
    "x = float(input('Print the first side of the triangle:'))\n",
    "y = float(input('Print the second side of the triangle:'))\n",
    "z = float(input('Print the third side of the triangle:'))\n",
    "\n",
    "print(\"The Triangle is:\",classify_triangle(a, b, c))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "faf8af52",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      ".....\n",
      "----------------------------------------------------------------------\n",
      "Ran 5 tests in 0.019s\n",
      "\n",
      "OK\n"
     ]
    }
   ],
   "source": [
    "import unittest\n",
    "class TestTriangle(unittest.TestCase):\n",
    "\n",
    "    def testSet1(self):\n",
    "        self.assertEqual(classify_triangle(1, 1, 1), \"Equilateral\", \"Should be Equilateral\")\n",
    "        self.assertNotEqual(classify_triangle(5, 5, 5), \"Isosceles\", \"Should be Equilateral\")\n",
    "        self.assertNotEqual(classify_triangle(3.0, 3.0, 3.0), \"Scalene\", \"Should be Equilateral\")\n",
    "        self.assertNotEqual(classify_triangle(6, 6, 6), \"Right\", \"Should be Equilateral\")\n",
    "        self.assertNotEqual(classify_triangle(1.5, 1.5, 1.5), \"Not a Triangle\", \"Should be Equilateral\")\n",
    "        \n",
    "    def testSet2(self):\n",
    "        self.assertEqual(classify_triangle(3, 3, 2), \"Isosceles\", \"Should be Isosceles\")\n",
    "        self.assertEqual(classify_triangle(3, 2, 3), \"Isosceles\", \"Should be Isosceles\")\n",
    "        self.assertEqual(classify_triangle(2, 3, 3), \"Isosceles\", \"Should be Isosceles\")\n",
    "        self.assertNotEqual(classify_triangle(4, 2, 4), \"Scalene\", \"Should be Isosceles\")\n",
    "        self.assertNotEqual(classify_triangle(5, 5, 3), \"Equilateral\", \"Should be Isosceles\")\n",
    "        self.assertNotEqual(classify_triangle(4, 4, 5.64), \"Right\", \"Should be Isosceles\")\n",
    "        self.assertNotEqual(classify_triangle(1, 3, 3), \"Not a Triangle\", \"Should be Isosceles\")\n",
    "        \n",
    "    def testSet3(self):\n",
    "        self.assertEqual(classify_triangle(1, 10, 12), \"Not a Triangle\", \"Should be Not a Triangle\")\n",
    "        self.assertNotEqual(classify_triangle(1, 1, 2), \"Isosceles\", \"Should be Not a Triangle\")\n",
    "        self.assertNotEqual(classify_triangle(3, 1.5, 1.5), \"Equilateral\", \"Should be Not a Triangle\")\n",
    "        self.assertNotEqual(classify_triangle(4, 2, 6), \"Right\", \"Should be Not a Triangle\")\n",
    "        self.assertNotEqual(classify_triangle(1, 4, 6), \"Scalene\", \"Should be Not a Triangle\")\n",
    "        \n",
    "    def testSet4(self):\n",
    "        self.assertEqual(classify_triangle(3, 4, 5), \"Right\", \"Should be Right\")\n",
    "        self.assertNotEqual(classify_triangle(12, 13, 5), \"Isosceles\", \"Should be Right\")\n",
    "        self.assertNotEqual(classify_triangle(10, 6, 8), \"Equilateral\", \"Should be Right\")\n",
    "        self.assertNotEqual(classify_triangle(4, 3, 5), \"Not a Triangle\", \"Should be Right\")\n",
    "        self.assertNotEqual(classify_triangle(12, 13, 5), \"Scalene\", \"Should be Right\")\n",
    "        \n",
    "    def testSet5(self):\n",
    "        self.assertEqual(classify_triangle(3, 10, 12), \"Scalene\", \"Should be Scalene\")\n",
    "        self.assertNotEqual(classify_triangle(1, 3, 2), \"Isosceles\", \"Should be Scalene\")\n",
    "        self.assertNotEqual(classify_triangle(3, 4, 1.5), \"Equilateral\", \"Should be Scalene\")\n",
    "        self.assertNotEqual(classify_triangle(4, 2, 6), \"Right\", \"Should be Scalene\")\n",
    "        self.assertNotEqual(classify_triangle(3, 4, 6), \"Not a Triangle\", \"Should be Scalene\")\n",
    "        \n",
    "if __name__ == '__main__':\n",
    "    unittest.main(argv=['first-arg-is-ignored'], exit=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70cffab0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

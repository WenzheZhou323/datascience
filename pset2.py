{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "pset2.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOqsKDsabzSKfzYF2AnMUXx",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/WenzheZhou323/datascience/blob/main/pset2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "id": "HDtIQPpIKvAc"
      },
      "outputs": [],
      "source": [
        "# Homework question 1\n",
        "def average(a1):\n",
        "  sum = 0\n",
        "  num = 0\n",
        "  for e in a1:\n",
        "    sum = sum + e\n",
        "    num = num + 1\n",
        "  return sum/num\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Homework question 2\n",
        "def common(a1, a2):\n",
        "  for a in a1:\n",
        "    temp = a\n",
        "    for b in a2:\n",
        "      if b == temp:\n",
        "        return True\n",
        "  return False\n"
      ],
      "metadata": {
        "id": "YKbJ0RZ8KyzT"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Homework question 3\n",
        "def zerooo(a):\n",
        "  for e in a:\n",
        "    if e == 0:\n",
        "      i = a.index(e)\n",
        "      a[i] = 'zerooo'"
      ],
      "metadata": {
        "id": "6KFRUG_dNlW9"
      },
      "execution_count": 12,
      "outputs": []
    }
  ]
}
# -*- coding: utf-8 -*-

# Michele Mattioni 
#
#Copyright Thu Jul 28 12:36:35 BST 2011 Michele Mattioni mattions@gmail.com
#
#This program is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#MA 02110-1301, USA.
#
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np


"""This is a quick hack to visualize the proposition dal _mobile all'immobile_ 
http://www.prossimaitalia.it/news/1273/dal-mobile-allimmobile/"""


def autolabel(rects, ax):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')
# Barchart

def plot_options(money_in_first_option, money_in_second_option, 
	money_out, in_milions=False):
	ind = np.arange(2)
	width = 0.35
	fig = plt.figure()
	ax = fig.add_subplot(111)
	if in_milions:
		money_in_first_option /= 1e6
		money_in_second_option /= 1e6
		money_out /= 1e6
		
	reacts1 = ax.bar(ind, (money_in_first_option, money_in_second_option), width, color='r')
	reacts2 = ax.bar(ind+width, (money_out, money_out), width, color='g')
	ax.set_xticks(ind+width)
	ax.set_xticklabels(('Tutte Case (1st opt)', 'Seconde e Terze Case (2nd opt)'))
	autolabel(reacts1, ax)
	autolabel(reacts2, ax)
	ax.legend((reacts1[0], reacts2[1]), ('Soldi in', 'Soldi out'), loc=0)
	ax.set_title("Proposta dall'immobile al mobile | prossimaitalia")
	ax.set_xlabel('http://bit.ly/imm2mob')
	if in_milions:
		ax.set_ylabel("Milioni di EUR")
		plt.ylim(0, 35e3)
		plt.savefig('immobile_to_mobile_mil.png')
		
	else:
		ax.set_ylabel("EUR")
		plt.ylim(0, 35e9)
		plt.savefig('immobile_to_mobile.png')

def plot_per_individual(contr_first, contr_second, received, year=12):
	ind = np.arange(2)
	width = 0.35
	fig = plt.figure()
	ax = fig.add_subplot(111)
	
	reacts1 = ax.bar(ind, (contr_first, contr_first * year), width, color='r')
	reacts2 = ax.bar(ind+width, (contr_second, contr_second * year), width, color='g')
	reacts3 = ax.bar(ind+width+width, (received, received * year), width, color='b')
	ax.set_xticks(ind+width+width)
	ax.set_xticklabels(('Mensile', 'Annuale'))
	autolabel(reacts1, ax)
	autolabel(reacts2, ax)
	autolabel(reacts3, ax)
	ax.legend((reacts1[0], reacts2[0], reacts3[0]), ('Contributo Tutte Case (1st opt)', 
													 'Contributo Seconde e Terze Case (2st opt)',
													 'Assegno'), loc=0)
	ax.set_title("Proposta dall'immobile al mobile | prossimaitalia")
	ax.set_xlabel('http://bit.ly/imm2mob')
	plt.savefig('immobile_to_mobile_mil.png')
	ax.set_ylabel("EUR")
	plt.ylim(0, 2000)
	plt.savefig('immobile_to_mobile_individuale.png')		




if __name__ == '__main__':
	##################### 
	# Vars

	workers = 23e6
	minimal_pension = 4e6
	# money out
	annual_cheque = 550 # EUR
	money_out = annual_cheque * (minimal_pension + workers)
	year = 12

	# first option vars
	total_houses = 32e6
	contribution_in_month_first_option = 40 # EUR
	money_in_first_option = total_houses * (contribution_in_month_first_option * year)

	# second option vars
	second_houses = 12e6
	third_houses = 12e6
	contribution_in_month_second_option = 100 # EUR
	money_in_second_option = (second_houses + third_houses) * (contribution_in_month_second_option * year)

	plot_options(money_in_first_option, money_in_second_option, money_out)
	plot_options(money_in_first_option, money_in_second_option, 
		money_out, in_milions=True)
	
	plot_per_individual(contribution_in_month_first_option, 
						contribution_in_month_second_option,
						annual_cheque/year)

	plt.show()

#Check out README.txt under /opt/local/var/db/postgresql11 to start the server
#https://stackoverflow.com/questions/2732474
#(terminal) psql -U tinglin -d tinglin < aligulac.sql

import sys, math, datetime
import psycopg2
import pandas as pd
import numpy as np
import pickle

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec

if __name__ == "__main__":
    print("###############################################################################Tail")
    conn = None
    try:
        conn = psycopg2.connect("dbname='tinglin' user='tinglin' host='localhost' password='*'")
    except:
        print("ERROR: unable to connect to the server")
        raise
    cur = conn.cursor()

    #cur.execute("""SELECT * FROM pg_catalog.pg_tables;""")
    #cur.execute("""SELECT tag, id FROM player WHERE tag LIKE 'Se%' ORDER BY tag ASC;""")
    #cur.execute("""SELECT * FROM player WHERE tag = 'Serral';""")
    #rows = cur.fetchall(); print(rows)

    cur.execute("""SELECT period_id, bf_rating, position FROM rating \
                   WHERE player_id = 5414 ORDER BY period_id ASC;""")
    arr5414  = [list(tup) for tup in cur.fetchall()]
    cur.execute("""SELECT period_id, bf_rating, position FROM rating \
                   WHERE player_id = 5878 ORDER BY period_id ASC;""")
    arr5878  = [list(tup) for tup in cur.fetchall()]
    cur.execute("""SELECT period_id, bf_rating, position FROM rating \
                   WHERE player_id = 19591 ORDER BY period_id ASC;""")
    arr19591 = [list(tup) for tup in cur.fetchall()]

    per5414    = (np.array(arr5414)).T[0]
    rate5414   = (np.array(arr5414)).T[1]
    place5414  = (np.array(arr5414)).T[2]
    per5878    = (np.array(arr5878)).T[0]
    rate5878   = (np.array(arr5878)).T[1]
    place5878  = (np.array(arr5878)).T[2]
    per19591   = (np.array(arr19591)).T[0]
    rate19591  = (np.array(arr19591)).T[1]
    place19591 = (np.array(arr19591)).T[2]

    #plots
    fig = plt.figure(figsize=(12, 18))
    matplotlib.rc("xtick", labelsize=16)
    matplotlib.rc("ytick", labelsize=16)
    gs = gridspec.GridSpec(2, 1)
    ax = []
    for i in range (gs.nrows*gs.ncols): 
        ax.append(fig.add_subplot(gs[i]))
    fig.subplots_adjust(top=0.95, bottom=0.05, left=0.1, right=0.98)
   
    r5414  = ax[0].plot(per5414,  rate5414,  color="red",   linewidth=2)[0]
    r5878  = ax[0].plot(per5878,  rate5878,  color="blue",  linewidth=2)[0]
    r19591 = ax[0].plot(per19591, rate19591, color="green", linewidth=2)[0]
    ax[0].set_title("Rating from Aligulac", fontsize=24, y=1.03)
    ax[0].set_xlabel("period", fontsize=20)
    ax[0].set_ylabel("rating", fontsize=20)
    ax[0].legend([r5414, r5878, r19591], ["Reynor", "Clem", "MaxPax"],\
                 loc="upper left", fontsize=20)

    p5414  = ax[1].plot(per5414,  place5414,  color="red",   linewidth=2)[0]
    p5878  = ax[1].plot(per5878,  place5878,  color="blue",  linewidth=2)[0]
    p19591 = ax[1].plot(per19591, place19591, color="green", linewidth=2)[0]
    ax[1].set_title("Placement from Aligulac", fontsize=24, y=1.03)
    ax[1].set_xlabel("period", fontsize=20)
    ax[1].set_ylabel("placement", fontsize=20)
    ax[1].legend([p5414, p5878, p19591], ["Reynor", "Clem", "MaxPax"],\
                 loc="upper right", fontsize=20)

    figName = "rating_placement.png"
    plt.savefig(figName)
    plt.close(fig)
    print("Saving plot:\n ", figName)

    print("###############################################################################Tail")














 

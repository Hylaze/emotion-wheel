import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

def generate_shade(base_color, factor=0.2):
    """Lighten a color by mixing it with white."""
    base = to_rgb(base_color)
    return tuple((1 - factor) * c + factor for c in base)

def sunburst(nodes, total=np.pi * 2, offset=0, level=0, ax=plt.subplot(111, projection='polar'), color_map=None, parent_label=None, radius_per_level=[1, 3.5, 5, 5.5]):
    if level == 0: #draw inner circle
        ax.set_theta_direction(-1)
        ax.set_theta_zero_location('N')
        ax.set_axis_off()
        label, value, subnodes = nodes[0]
        ax.bar([0], [radius_per_level[0]], [np.pi * 2], color='white')
        ax.text(0, 0, label, ha='center', va='center',fontsize=5)
        sunburst(subnodes, total=value, level=level + 1, ax=ax, color_map=color_map,
                 parent_label=label, radius_per_level=radius_per_level)
        
    elif nodes:
        d = np.pi * 2 / total
        local_offset = offset
        labels, widths, sub_parents = [], [], []

        for label, value, subnodes in nodes:
            labels.append(label)
            widths.append(value * d)
            new_parent_label = label if level == 1 else parent_label
            sub_parents.append(new_parent_label)
            sunburst(subnodes, total=total, offset=local_offset, level=level + 1,
                     ax=ax, color_map=color_map, parent_label=new_parent_label,
                     radius_per_level=radius_per_level)
            local_offset += value

        values = np.cumsum([offset * d] + widths[:-1])
        height = radius_per_level[level] if level < len(radius_per_level) else 1
        bottom = sum(radius_per_level[:level]) if level < len(radius_per_level) else level
        heights = [height] * len(nodes)
        bottoms = [bottom] * len(nodes)

        # Color assignment
        colors = []
        for parent in sub_parents:
            base_color = color_map.get(parent, 'gray')
            if level > 1:
                colors.append(generate_shade(base_color, factor=0.2 * level))
            else:
                colors.append(base_color)
        # Label text
        rects = ax.bar(values, heights, widths, bottoms, linewidth=0.5,
                       edgecolor='black', align='edge', color=colors)
        for rect, label in zip(rects, labels):
            x = rect.get_x() + rect.get_width() / 2
            y = rect.get_y() + rect.get_height() / 2
            rotation = (90 + (360 - np.degrees(x))) % 360
            ax.text(x, y, label, rotation=rotation, ha='center', va='center',fontsize=5)

converted_data = [
    ('', 100, [
        ('traurig', 100/6, [
            ('enttäuscht', 100/6/7, [
                ('ernüchtert', 100/6/7/2, []),
                ('unzufrieden', 100/6/7/2, [])
            ]),
            ('elend', 100/6/7, [
                ('miserabel', 100/6/7/2, []),
                ('jämmerlich', 100/6/7/2, [])
            ]),
            ('verzweifelt', 100/6/7, [
                ('deprimiert', 100/6/7/2, []),
                ('hoffnungslos', 100/6/7/2, [])
            ]),
            ('einsam', 100/6/7, [
                ('verlassen', 100/6/7/2, []),
                ('zurückgezogen', 100/6/7/2, [])
            ]),
            ('schuldbewusst', 100/6/7, [
                ('betreten', 100/6/7/2, []),
                ('verlegen', 100/6/7/2, [])
            ]),
            ('mutlos', 100/6/7, [
                ('resigniert', 100/6/7/2, []),
                ('verzagt', 100/6/7/2, [])
            ]),
            ('bedrückt', 100/6/7, [
                ('niedergeschlagen', 100/6/7/2, []),
                ('betrübt', 100/6/7/2, [])
            ])
        ]),
        ('überrascht', 100/6, [
            ('erstaunt', 100/6/4, [
                ('fassungslos', 100/6/4/2, []),
                ('verwundert', 100/6/4/2, [])
            ]),
            ('erschrocken', 100/6/4, [
                ('bestürzt', 100/6/4/2, []),
                ('entsetzt', 100/6/4/2, [])
            ]),
            ('verwirrt', 100/6/4, [
                ('entgeistert', 100/6/4/2, []),
                ('verstört', 100/6/4/2, [])
            ]),
            ('gespannt', 100/6/4, [
                ('neugierig', 100/6/4/2, []),
                ('wissbegierig', 100/6/4/2, [])
            ])
        ]),
        ('ängstlich', 100/6, [
            ('gedemütigt', 100/6/7, [
                ('erniedrigt', 100/6/7/2, []),
                ('beschämt', 100/6/7/2, [])
            ]),
            ('zurückgewiesen', 100/6/7, [
                ('abgelehnt', 100/6/7/2, []),
                ('verachtet', 100/6/7/2, [])
            ]),
            ('unsicher', 100/6/7, [
                ('schüchtern', 100/6/7/2, []),
                ('scheu', 100/6/7/2, [])
            ]),
            ('besorgt', 100/6/7, [
                ('furchtsam', 100/6/7/2, []),
                ('bange', 100/6/7/2, [])
            ]),
            ('unterwürfig', 100/6/7, [
                ('demütig', 100/6/7/2, []),
                ('folgsam', 100/6/7/2, [])
            ]),
            ('verschreckt', 100/6/7, [
                ('zaghaft', 100/6/7/2, []),
                ('verängstigt', 100/6/7/2, [])
            ]),
            ('bedroht', 100/6/7, [
                ('gefährdet', 100/6/7/2, []),
                ('bedrängt', 100/6/7/2, [])
            ])
        ]),
        ('glücklich', 100/6, [
            ('fröhlich', 100/6/7, [
                ('vergnügt', 100/6/7/2, []),
                ('beschwingt', 100/6/7/2, [])
            ]),
            ('zufrieden', 100/6/7, [
                ('ausgeglichen', 100/6/7/2, []),
                ('gelassen', 100/6/7/2, [])
            ]),
            ('freudig', 100/6/7, [
                ('selig', 100/6/7/2, []),
                ('beglückt', 100/6/7/2, [])
            ]),
            ('optimistisch', 100/6/7, [
                ('zuversichtlich', 100/6/7/2, []),
                ('hoffnungsvoll', 100/6/7/2, [])
            ]),
            ('erwartungsvoll', 100/6/7, [
                ('aufgeregt', 100/6/7/2, []),
                ('aufgeschlossen', 100/6/7/2, [])
            ]),
            ('stolz', 100/6/7, [
                ('selbstsicher', 100/6/7/2, []),
                ('würdevoll', 100/6/7/2, [])
            ]),
            ('erleichtert', 100/6/7, [
                ('beruhigt', 100/6/7/2, []),
                ('gelöst', 100/6/7/2, [])
            ])
        ]),
        ('ablehnend', 100/6, [
            ('abwertend', 100/6/4, [
                ('abschätzig', 100/6/4/2, []),
                ('verächtlich', 100/6/4/2, [])
            ]),
            ('lustlos', 100/6/4, [
                ('träge', 100/6/4/2, []),
                ('unwillig', 100/6/4/2, [])
            ]),
            ('abgestoßen', 100/6/4, [
                ('angeekelt', 100/6/4/2, []),
                ('angewidert', 100/6/4/2, [])
            ]),
            ('abweisend', 100/6/4, [
                ('widerstrebend', 100/6/4/2, []),
                ('missbilligend', 100/6/4/2, [])
            ])
        ]),
        ('ärgerlich', 100/6, [
            ('wütend', 100/6/7, [
                ('grimmig', 100/6/7/2, []),
                ('zornig', 100/6/7/2, [])
            ]),
            ('aggressiv', 100/6/7, [
                ('hasserfüllt', 100/6/7/2, []),
                ('angriffslustig', 100/6/7/2, [])
            ]),
            ('kritisch', 100/6/7, [
                ('abfällig', 100/6/7/2, []),
                ('vorwurfsvoll', 100/6/7/2, [])
            ]),
            ('distanziert', 100/6/7, [
                ('reserviert', 100/6/7/2, []),
                ('unnahbar', 100/6/7/2, [])
            ]),
            ('verletzt', 100/6/7, [
                ('getroffen', 100/6/7/2, []),
                ('gekränkt', 100/6/7/2, [])
            ]),
            ('böse', 100/6/7, [
                ('sauer', 100/6/7/2, []),
                ('erzürnt', 100/6/7/2, [])
            ]),
            ('frustriert', 100/6/7, [
                ('desillusioniert', 100/6/7/2, []),
                ('verbittert', 100/6/7/2, [])
            ])
        ])
    ])
]

feelings_data = {
    "traurig": {
        "enttäuscht": ["ernüchtert", "unzufrieden"],
        "elend": ["miserabel", "jämmerlich"],
        "verzweifelt": ["deprimiert", "hoffnungslos"],
        "einsam": ["verlassen", "zurückgezogen"],
        "schuldbewusst": ["betreten", "verlegen"],
        "mutlos": ["resigniert", "verzagt"],
        "bedrückt": ["niedergeschlagen", "betrübt"]
    },
    "überrascht": {
        "erstaunt": ["fassungslos", "verwundert"],
        "erschrocken": ["bestürzt", "entsetzt"],
        "verwirrt": ["entgeistert", "verstört"],
        "gespannt": ["neugierig", "wissbegierig"]
    },
    "ängstlich": {
        "gedemütigt": ["erniedrigt", "beschämt"],
        "zurückgewiesen": ["miserabel", "jämmerlich"],
        "unsicher": ["schüchtern", "scheu"],
        "besorgt": ["furchtsam", "bange"],
        "unterwürfig": ["demütig", "folgsam"],
        "verschreckt": ["zaghaft", "verängstigt"],
        "bedroht": ["gefährdet", "bedrängt"]
    },
    "glücklich": {
        "fröhlich": ["erniedrigt", "beschämt"],
        "zufrieden": ["miserabel", "jämmerlich"],
        "freudig": ["schüchtern", "scheu"],
        "optimistisch": ["furchtsam", "bange"],
        "sorglos": ["demütig", "folgsam"],
        "erwartungsvoll": ["zaghaft", "verängstigt"],
        "stolz": ["gefährdet", "bedrängt"],
        "erleichtert": ["beruhigt", "gelöst"]
    },
    "ablehnend": {
        "abwertend": ["abschätzig", "verächtlich"],
        "lustlos": ["träge", "unwillig"],
        "abgestoßen": ["angeekelt", "angewidert"],
        "abweisend": ["widerstrebend", "missbilligend"]
    },
    "ärgerlich": {
        "wütend": ["grimmig", "zornig"],
        "aggressiv": ["hasserfüllt", "angriffslustig"],
        "kritisch": ["abfällig", "vorwurfsvoll"],
        "distanziert": ["reserviert", "unnahbar"],
        "verletzt": ["getroffen", "gekränkt"],
        "böse": ["sauer", "erzürnt"],
        "frustriert": ["desillusioniert", "verbittert"]
    },
}

custom_color_map = {
    'traurig': '#5569a4',
    'glücklich': '#5bb666',
    'ängstlich': '#ef7931',
    'überrascht': '#e5bf00',
    'ablehnend': '#8f5eb3',
    'ärgerlich': '#9d416e'    
}
sunburst(converted_data,color_map=custom_color_map)

plt.rcParams["figure.figsize"] = (20, 20)
plt.savefig('emotion_wheel_2.pdf',bbox_inches='tight', dpi=600)
plt.show()
# clue_data.py

# Themes and word lists
THEMES = {
    "animals": [
        "elephant", "tiger", "kangaroo", "penguin", "dolphin",
        "giraffe", "octopus", "crocodile", "panda", "wolf"
    ],
    "fruits": [
        "apple", "banana", "cherry", "grape", "pineapple",
        "mango", "strawberry", "blueberry", "watermelon", "peach"
    ],
    "countries": [
        "france", "brazil", "canada", "japan", "germany",
        "italy", "russia", "mexico", "india", "egypt"
    ],
    "instruments": [
        "guitar", "piano", "violin", "drums", "flute",
        "saxophone", "trumpet", "harp", "cello", "clarinet"
    ],
    "planets": [
        "mercury", "venus", "earth", "mars", "jupiter",
        "saturn", "uranus", "neptune", "pluto", "ceres"
    ],
    "colors": [
        "red", "blue", "green", "yellow", "purple",
        "orange", "pink", "brown", "black", "white"
    ],
    "sports": [
        "soccer", "basketball", "tennis", "baseball", "golf",
        "boxing", "cricket", "swimming", "cycling", "volleyball"
    ],
    "jobs": [
        "teacher", "doctor", "engineer", "chef", "artist",
        "pilot", "nurse", "firefighter", "police", "musician"
    ],
    # New themes:
    "vehicles": [
        "car", "bicycle", "airplane", "train", "boat",
        "motorcycle", "bus", "helicopter", "submarine", "truck"
    ],
    "mythology": [
        "zeus", "odin", "anubis", "poseidon", "hades",
        "thor", "ares", "isis", "kraken", "phoenix"
    ],
    "technology": [
        "computer", "smartphone", "robot", "drone", "satellite",
        "internet", "server", "algorithm", "database", "chip"
    ],
    "languages": [
        "english", "spanish", "french", "mandarin", "arabic",
        "hindi", "russian", "portuguese", "japanese", "german"
    ]
}

# Clues dictionary with three unique vague and helpful clues per word.
CLUES = {
    # Animals
    "elephant": {
        "vague": [
            "A massive creature roaming vast lands.",
            "Often pictured as a gentle giant of the wild.",
            "A symbol of memory and ancient wisdom."
        ],
        "helpful": [
            "It has a long trunk and large, flapping ears.",
            "Famous for its impressive size and tusks.",
            "Its social herds and iconic features set it apart."
        ]
    },
    "tiger": {
        "vague": [
            "A stealthy feline that stalks in the shadows.",
            "Often depicted in legends of power and mystery.",
            "A solitary creature with an enigmatic allure."
        ],
        "helpful": [
            "It sports bold stripes and a lithe frame.",
            "A native of dense jungles with piercing eyes.",
            "Its distinctive coat and fierce nature are well-known."
        ]
    },
    "kangaroo": {
        "vague": [
            "A bouncy creature from a faraway land.",
            "Often linked to wide, open terrains and unique hops.",
            "A marsupial known more by its silhouette than details."
        ],
        "helpful": [
            "It carries its young in a pouch with care.",
            "Noted for its powerful hind legs and unique gait.",
            "A classic emblem of distant, sunburnt landscapes."
        ]
    },
    "penguin": {
        "vague": [
            "A flightless bird with a quirky, waddling walk.",
            "Often envisioned in icy, remote settings.",
            "A creature that dresses in nature’s own tuxedo."
        ],
        "helpful": [
            "It thrives in frigid climates and icy waters.",
            "Recognized for its social nature and distinct gait.",
            "Its black-and-white appearance is unmistakable."
        ]
    },
    "dolphin": {
        "vague": [
            "A sleek marine dweller with a playful edge.",
            "Often seen as a symbol of intelligence in the sea.",
            "A creature that glides gracefully through the waves."
        ],
        "helpful": [
            "It uses echolocation to navigate underwater.",
            "Famous for its acrobatic leaps and friendly behavior.",
            "Its streamlined body is built for swift swimming."
        ]
    },
    "giraffe": {
        "vague": [
            "A towering creature with a uniquely elongated form.",
            "Often associated with sunlit savannas and treetops.",
            "A gentle giant that stands out from the herd."
        ],
        "helpful": [
            "It uses its height to reach leaves high in trees.",
            "Known for its patchy coat and graceful stride.",
            "Its long neck is one of its most defining features."
        ]
    },
    "octopus": {
        "vague": [
            "A mysterious denizen of the deep blue.",
            "Often shrouded in tales of ink and escape.",
            "A shape-shifting creature with fluid movements."
        ],
        "helpful": [
            "It possesses eight arms and an agile body.",
            "Notable for its ability to camouflage in an instant.",
            "Its ink defense mechanism is a natural marvel."
        ]
    },
    "crocodile": {
        "vague": [
            "A stealthy reptile lurking in murky waters.",
            "Often thought of as a relic from prehistoric times.",
            "A creature that blends silently into its swampy home."
        ],
        "helpful": [
            "It has a powerful bite armed with sharp teeth.",
            "Known for its armored skin and ambush tactics.",
            "Its cold-blooded nature makes it a formidable hunter."
        ]
    },
    "panda": {
        "vague": [
            "A fuzzy creature with a penchant for bamboo.",
            "Often seen as a cuddly symbol of conservation.",
            "A rare and gentle animal with a monochrome look."
        ],
        "helpful": [
            "It primarily feeds on bamboo in its natural habitat.",
            "Noted for its slow, deliberate movements and charm.",
            "Its distinctive black-and-white fur is iconic."
        ]
    },
    "wolf": {
        "vague": [
            "A wild creature known to roam in tight-knit groups.",
            "Often wrapped in legends of loyalty and mystery.",
            "A shadowy figure of the untamed wilderness."
        ],
        "helpful": [
            "It has keen senses and a powerful howl.",
            "Known for its strong pack dynamics and hunting skills.",
            "Its elusive nature and survival tactics are renowned."
        ]
    },

    # Fruits
    "apple": {
        "vague": [
            "A common fruit that hides a world of symbolism.",
            "Often seen as a crisp and familiar treat.",
            "A round fruit with a hint of the forbidden."
        ],
        "helpful": [
            "It is crisp, juicy, and comes in red or green.",
            "A symbol of health that features in many tales.",
            "Its simple shape and sweet taste are well-known."
        ]
    },
    "banana": {
        "vague": [
            "A curvy fruit with a tropical mystery.",
            "Often associated with a carefree, sunny vibe.",
            "A long, yellow treat that’s as playful as it seems."
        ],
        "helpful": [
            "It has a peel that must be removed to enjoy its flesh.",
            "Known for its sweet, soft texture and distinctive curve.",
            "Its vibrant color and tropical origin are unmistakable."
        ]
    },
    "cherry": {
        "vague": [
            "A tiny fruit that packs a secret punch.",
            "Often regarded as a delicate morsel of nature.",
            "A small red dot in a world of flavors."
        ],
        "helpful": [
            "It typically grows in pairs and adds a burst of tartness.",
            "Noted for its bright hue and jewel-like appearance.",
            "Its flavor is both sweet and a touch tangy."
        ]
    },
    "grape": {
        "vague": [
            "A small orb that clusters like hidden treasures.",
            "Often evoking images of vineyards and summer days.",
            "A diminutive fruit that comes in tight bunches."
        ],
        "helpful": [
            "It is juicy and can be eaten fresh or dried into raisins.",
            "Known for its sweetness and use in winemaking.",
            "Its delicate skin and burst of flavor are classic."
        ]
    },
    "pineapple": {
        "vague": [
            "A spiky tropical enigma with a sweet secret.",
            "Often seen as an exotic burst of flavor.",
            "A rough exterior that guards a luscious heart."
        ],
        "helpful": [
            "It has a fibrous exterior with juicy, tangy flesh.",
            "Known for its crown-like top and unique taste.",
            "Its blend of sweet and tart notes makes it stand out."
        ]
    },
    "mango": {
        "vague": [
            "A luscious tropical fruit that hints at paradise.",
            "Often evoking warm, sun-drenched memories.",
            "A soft, juicy treat wrapped in mystery."
        ],
        "helpful": [
            "It has a large pit and richly sweet, fragrant flesh.",
            "Famous for its smooth texture and vibrant color.",
            "Its tropical taste and aroma are hard to forget."
        ]
    },
    "strawberry": {
        "vague": [
            "A small red fruit that seems to whisper sweetness.",
            "Often associated with summer picnics and gentle charm.",
            "A heart-shaped delight that hints at freshness."
        ],
        "helpful": [
            "It sports tiny seeds on its surface and a juicy core.",
            "Known for its blend of sweetness with a hint of tartness.",
            "Its familiar red hue and delicate flavor are beloved."
        ]
    },
    "blueberry": {
        "vague": [
            "A petite, mysterious orb with a deep hue.",
            "Often seen as nature’s tiny, blue jewel.",
            "A small fruit that bursts with understated charm."
        ],
        "helpful": [
            "It is rich in antioxidants and subtle in sweetness.",
            "Commonly used in desserts and smoothies for its flavor.",
            "Its deep blue color and soft texture are distinctive."
        ]
    },
    "watermelon": {
        "vague": [
            "A colossal fruit synonymous with summer fun.",
            "Often evoking images of picnics and cooling refreshment.",
            "A green-skinned enigma hiding a scarlet secret."
        ],
        "helpful": [
            "It has a thick rind with juicy, red flesh inside.",
            "Known for its high water content and refreshing bite.",
            "Its striking contrast of colors makes it unmistakable."
        ]
    },
    "peach": {
        "vague": [
            "A fuzzy fruit that exudes a gentle sweetness.",
            "Often linked to warm, lazy summer afternoons.",
            "A soft, blushing fruit with a tender secret."
        ],
        "helpful": [
            "It has a delicate texture and a central pit.",
            "Known for its fragrant aroma and tender bite.",
            "Its unique blend of softness and tang is memorable."
        ]
    },

    # Countries
    "france": {
        "vague": [
            "A European nation wrapped in art and romance.",
            "Often imagined as a land of elegant mystery.",
            "A country where history and style merge effortlessly."
        ],
        "helpful": [
            "It is famed for its cuisine, wine, and iconic landmarks.",
            "Home to timeless symbols like the Eiffel Tower.",
            "Its cultural allure and artistic heritage are celebrated."
        ]
    },
    "brazil": {
        "vague": [
            "A vast land pulsing with rhythm and color.",
            "Often conjuring images of lush rainforests and festivals.",
            "A nation where nature and passion dance together."
        ],
        "helpful": [
            "It boasts vibrant traditions like Carnival and football.",
            "Known for its diverse landscapes and spirited culture.",
            "Its natural wonders and festive energy are renowned."
        ]
    },
    "canada": {
        "vague": [
            "A sprawling land of natural beauty and cool vibes.",
            "Often envisioned as a mosaic of wilderness and modernity.",
            "A country that whispers of snowy peaks and green forests."
        ],
        "helpful": [
            "It is known for its maple leaf and friendly communities.",
            "Famous for its breathtaking landscapes and outdoor lifestyle.",
            "Its blend of nature and urban charm appeals widely."
        ]
    },
    "japan": {
        "vague": [
            "A land where ancient tradition meets futuristic dreams.",
            "Often seen as a delicate balance of old and new.",
            "A country with quiet rituals and vibrant innovation."
        ],
        "helpful": [
            "It is celebrated for its art, cuisine, and cultural finesse.",
            "Home to time-honored practices like tea ceremonies.",
            "Its unique blend of history and modernity enchants many."
        ]
    },
    "germany": {
        "vague": [
            "A European country with a legacy of precision and lore.",
            "Often associated with robust industry and rich heritage.",
            "A nation where modernity meets storied traditions."
        ],
        "helpful": [
            "It is renowned for its engineering, beer, and castles.",
            "Famous for contributions to music, philosophy, and art.",
            "Its blend of tradition and innovation is widely respected."
        ]
    },
    "italy": {
        "vague": [
            "A country steeped in timeless art and flavor.",
            "Often conjuring images of cobbled streets and ancient ruins.",
            "A land where culinary and cultural tales unfold."
        ],
        "helpful": [
            "It is famous for its pasta, pizza, and historical marvels.",
            "Home to the Renaissance and eternal landmarks.",
            "Its rich culture and cuisine make it a global icon."
        ]
    },
    "russia": {
        "vague": [
            "A vast nation draped in wintry mystery.",
            "Often portrayed as both rugged and poetic.",
            "A land where cold landscapes meet epic legends."
        ],
        "helpful": [
            "It is known for its literature, ballet, and icy expanses.",
            "A country of contrasts, from vibrant cities to frozen tundras.",
            "Its cultural and historical impact resonates worldwide."
        ]
    },
    "mexico": {
        "vague": [
            "A country of vivid colors and enduring traditions.",
            "Often remembered for its lively festivals and heritage.",
            "A land where ancient ruins meet modern rhythms."
        ],
        "helpful": [
            "It is known for its rich cuisine, music, and history.",
            "Famous for its spicy flavors and warm hospitality.",
            "Its cultural mosaic and vibrant celebrations are renowned."
        ]
    },
    "india": {
        "vague": [
            "A land of endless contrasts and ancient tales.",
            "Often associated with vibrant chaos and mystique.",
            "A country where tradition and modernity coexist."
        ],
        "helpful": [
            "It is celebrated for its spices, festivals, and cinema.",
            "Home to diverse cultures and timeless traditions.",
            "Its rich heritage and dynamic growth captivate many."
        ]
    },
    "egypt": {
        "vague": [
            "An ancient land filled with timeless secrets.",
            "Often shrouded in myths of pharaohs and pyramids.",
            "A country where history and legend intertwine."
        ],
        "helpful": [
            "It is known for its monumental pyramids and the Nile.",
            "Famous for its ancient artifacts and storied past.",
            "Its archaeological wonders continue to fascinate the world."
        ]
    },

    # Instruments
    "guitar": {
        "vague": [
            "A string instrument that hums with rustic charm.",
            "Often seen as the soul of campfire ballads.",
            "A tool for strumming memories into melody."
        ],
        "helpful": [
            "It typically features six strings and a wooden body.",
            "Favored for its versatility across many music genres.",
            "Its sound is produced by plucking or strumming the strings."
        ]
    },
    "piano": {
        "vague": [
            "A keyboard instrument that resonates with elegance.",
            "Often envisioned as the heart of classical tunes.",
            "A grand presence in the world of harmony."
        ],
        "helpful": [
            "It has black and white keys that create a range of sounds.",
            "Played by striking keys to produce layered chords.",
            "Its dynamic range makes it a favorite in many genres."
        ]
    },
    "violin": {
        "vague": [
            "A small string instrument with a soulful cry.",
            "Often associated with delicate, emotional melodies.",
            "A slender instrument that sings with passion."
        ],
        "helpful": [
            "It is played with a bow to produce a haunting tone.",
            "Known for its expressive vibrato and rich timbre.",
            "Its portability and charm make it a classic choice."
        ]
    },
    "drums": {
        "vague": [
            "A rhythmic instrument that echoes deep beats.",
            "Often found setting the pace in lively gatherings.",
            "A percussive heartbeat in the realm of music."
        ],
        "helpful": [
            "It is played by striking surfaces with sticks or hands.",
            "Known for creating the foundational rhythm in music.",
            "Its dynamic sounds drive the tempo and energy of a song."
        ]
    },
    "flute": {
        "vague": [
            "A slender woodwind that whispers light melodies.",
            "Often associated with airy tunes and soft echoes.",
            "A simple instrument that floats in the soundscape."
        ],
        "helpful": [
            "It is played by blowing across an opening to create sound.",
            "Known for its clear, high-pitched tone.",
            "Its gentle timbre makes it a subtle musical voice."
        ]
    },
    "saxophone": {
        "vague": [
            "A curvy brass instrument with a soulful vibe.",
            "Often linked to smooth jazz and late-night moods.",
            "A musical tool that exudes cool and emotion."
        ],
        "helpful": [
            "It produces sound through a single-reed mouthpiece.",
            "Renowned for its warm, expressive tone.",
            "Its unique design contributes to a distinctive, jazzy sound."
        ]
    },
    "trumpet": {
        "vague": [
            "A compact brass instrument with a bold flair.",
            "Often heard in fanfares and energetic anthems.",
            "A small powerhouse in the realm of brass."
        ],
        "helpful": [
            "It is played by blowing into a cup-shaped mouthpiece.",
            "Known for its bright, piercing tone in ensembles.",
            "Its commanding sound stands out in any musical setting."
        ]
    },
    "harp": {
        "vague": [
            "A majestic string instrument with a dreamy aura.",
            "Often associated with legends and ethereal tunes.",
            "A large, graceful instrument that evokes calm."
        ],
        "helpful": [
            "It is played by plucking strings with delicate fingers.",
            "Known for its rich, resonant sound and elegant design.",
            "Its gentle chords create a serene musical backdrop."
        ]
    },
    "cello": {
        "vague": [
            "A deep, resonant string instrument with a somber tone.",
            "Often seen as the voice of melancholy in music.",
            "A large instrument that exudes warm, rich notes."
        ],
        "helpful": [
            "It is played with a bow to create a deep, velvety sound.",
            "Renowned for its rich timbre in orchestral pieces.",
            "Its lower registers add depth and emotion to music."
        ]
    },
    "clarinet": {
        "vague": [
            "A woodwind instrument with a soft, fluid character.",
            "Often heard weaving subtle melodies in ensembles.",
            "A slender instrument that offers a gentle whisper."
        ],
        "helpful": [
            "It uses a reed to generate a smooth, mellow sound.",
            "Known for its versatility in both classical and jazz settings.",
            "Its agile response makes it a favorite for intricate tunes."
        ]
    },

    # Planets
    "mercury": {
        "vague": [
            "A small, scorched world closest to the sun.",
            "Often depicted as a swift, rocky wanderer.",
            "A celestial body with extreme contrasts in temperature."
        ],
        "helpful": [
            "It has a cratered surface and negligible atmosphere.",
            "Its rapid orbit makes it one of the fastest planets.",
            "Its proximity to the sun results in dramatic heat swings."
        ]
    },
    "venus": {
        "vague": [
            "A bright, enigmatic planet cloaked in clouds.",
            "Often shrouded in a mysterious, golden glow.",
            "A world that remains hidden behind thick veils."
        ],
        "helpful": [
            "It is enveloped by dense, reflective clouds.",
            "Known for its extreme greenhouse conditions.",
            "Its surface remains obscured by a constant, toxic haze."
        ]
    },
    "earth": {
        "vague": [
            "Our blue home teeming with life and mystery.",
            "A vibrant orb of water and land in the cosmos.",
            "A unique planet where nature thrives in abundance."
        ],
        "helpful": [
            "It supports a diverse array of ecosystems and climates.",
            "Its oceans, continents, and atmosphere create a balanced home.",
            "Its life-sustaining features make it singular in our solar system."
        ]
    },
    "mars": {
        "vague": [
            "A ruddy world that sparks dreams of exploration.",
            "Often seen as a dusty, ancient relic of space.",
            "A barren landscape that hints at long-lost water flows."
        ],
        "helpful": [
            "It is renowned for its red hue and rocky surface.",
            "Often called the 'Red Planet' due to its color.",
            "Its terrain shows evidence of ancient riverbeds."
        ]
    },
    "jupiter": {
        "vague": [
            "A colossal gas giant dominating the night sky.",
            "Often depicted as a swirling, majestic orb.",
            "A giant that commands attention with its stormy presence."
        ],
        "helpful": [
            "It is the largest planet with a famous, long-lasting storm.",
            "Known for its numerous moons and turbulent atmosphere.",
            "Its massive size makes it a gravitational anchor in the solar system."
        ]
    },
    "saturn": {
        "vague": [
            "A regal gas giant adorned with stunning rings.",
            "Often celebrated for its elegant, banded appearance.",
            "A celestial wonder that enchants with its orbiting bands."
        ],
        "helpful": [
            "It boasts a spectacular ring system made of ice and rock.",
            "Famous for its array of moons and striking visual features.",
            "Its rings and gentle hues make it an icon of beauty."
        ]
    },
    "uranus": {
        "vague": [
            "A distant, tilted world with an offbeat spin.",
            "Often seen as mysterious due to its unusual axis.",
            "A chilly planet with a sideways glance at the stars."
        ],
        "helpful": [
            "It rotates on its side, creating extreme seasonal shifts.",
            "Known for its subtle rings and pale blue tint.",
            "Its unconventional tilt sets it apart from its neighbors."
        ]
    },
    "neptune": {
        "vague": [
            "A deep blue world swirling with icy mysteries.",
            "Often depicted as a remote, stormy giant.",
            "A planet that exudes a cold, mesmerizing charm."
        ],
        "helpful": [
            "It is celebrated for its intense blue color and windy storms.",
            "Famous for its dynamic weather patterns far from the sun.",
            "Its vivid hues and turbulent atmosphere make it unique."
        ]
    },
    "pluto": {
        "vague": [
            "A tiny, icy wanderer at the edge of the known.",
            "Often regarded as a mysterious outlier of the solar system.",
            "A cold, distant world that defies simple classification."
        ],
        "helpful": [
            "It was once considered the ninth planet before reclassification.",
            "Noted for its diminutive size and remote orbit.",
            "Its status as a dwarf planet remains a topic of debate."
        ]
    },
    "ceres": {
        "vague": [
            "A modest body nestled in the asteroid belt.",
            "Often seen as a bridge between planets and rocks.",
            "A small orb that quietly orbits among space debris."
        ],
        "helpful": [
            "It is the largest object in the asteroid belt.",
            "Known for its unique features that blur planetary lines.",
            "Its rocky surface and position spark curiosity among astronomers."
        ]
    },

    # Colors
    "red": {
        "vague": [
            "A bold hue that demands attention without words.",
            "Often associated with passion, danger, and energy.",
            "A striking color that leaves a lasting impression."
        ],
        "helpful": [
            "It is one of the primary colors, vibrant and intense.",
            "Often used to symbolize strong emotions or warnings.",
            "Its prominence in nature and art makes it unforgettable."
        ]
    },
    "blue": {
        "vague": [
            "A cool shade that soothes and intrigues the eye.",
            "Often linked to endless skies and deep oceans.",
            "A color that quietly evokes calm and mystery."
        ],
        "helpful": [
            "It is a primary color known for its serene qualities.",
            "Commonly used to represent depth and stability.",
            "Its soft, calming nature is found in many natural scenes."
        ]
    },
    "green": {
        "vague": [
            "A color that whispers of nature and fresh beginnings.",
            "Often evoking images of forests and verdant fields.",
            "A hue that suggests growth without giving too much away."
        ],
        "helpful": [
            "It is associated with life, renewal, and natural beauty.",
            "Commonly seen in foliage and natural landscapes.",
            "Its soothing presence is a staple in organic designs."
        ]
    },
    "yellow": {
        "vague": [
            "A bright shade that hints at warmth and light.",
            "Often reminiscent of soft, glowing sunshine.",
            "A gentle burst of color that lifts the mood."
        ],
        "helpful": [
            "It is a primary color that radiates warmth and optimism.",
            "Often used to evoke feelings of cheerfulness and energy.",
            "Its luminous quality makes it a favorite in many designs."
        ]
    },
    "purple": {
        "vague": [
            "A deep, mysterious hue that flirts with luxury.",
            "Often linked to creativity and subtle magic.",
            "A color that carries an air of enigma and grace."
        ],
        "helpful": [
            "It is historically associated with royalty and mysticism.",
            "Often used to suggest creativity and a touch of the exotic.",
            "Its uncommon nature sets it apart in a vivid palette."
        ]
    },
    "orange": {
        "vague": [
            "A vibrant tone that radiates energy and fun.",
            "Often evoking images of sunsets and autumn leaves.",
            "A lively color that hints at warmth without being overt."
        ],
        "helpful": [
            "It is a blend of red and yellow, exuding bold energy.",
            "Commonly used to inspire enthusiasm and creativity.",
            "Its brightness makes it a memorable accent in design."
        ]
    },
    "pink": {
        "vague": [
            "A soft, playful color that flirts with charm.",
            "Often linked to tender moments and lighthearted fun.",
            "A gentle shade that is both subtle and inviting."
        ],
        "helpful": [
            "It is a delicate hue often used to evoke warmth and affection.",
            "Commonly seen in nature’s softer expressions and creative art.",
            "Its understated tone adds a touch of whimsy to any design."
        ]
    },
    "brown": {
        "vague": [
            "A warm, earthy tone that feels natural and grounded.",
            "Often associated with rustic charm and reliability.",
            "A color that evokes the essence of wood and earth."
        ],
        "helpful": [
            "It is common in nature, symbolizing stability and comfort.",
            "Often used to represent organic materials and tradition.",
            "Its natural vibe makes it a subtle background for other colors."
        ]
    },
    "black": {
        "vague": [
            "A classic, mysterious hue that absorbs all light.",
            "Often linked to elegance and understated power.",
            "A color that speaks volumes without saying a word."
        ],
        "helpful": [
            "It is a timeless color often associated with sophistication.",
            "Used to evoke depth, formality, and modern style.",
            "Its stark simplicity makes it both versatile and striking."
        ]
    },
    "white": {
        "vague": [
            "A clean, pure color that opens up any space.",
            "Often seen as a blank canvas full of possibility.",
            "A neutral tone that quietly complements any palette."
        ],
        "helpful": [
            "It is associated with simplicity, clarity, and fresh starts.",
            "Often used as a background to make other colors pop.",
            "Its unassuming nature makes it a universal design choice."
        ]
    },

    # Sports
    "soccer": {
        "vague": [
            "A globally adored game played on lush, green fields.",
            "Often seen as a dance of strategy and spontaneous play.",
            "A sport that unites fans through simple, fast-paced action."
        ],
        "helpful": [
            "It involves two teams trying to score by kicking a ball.",
            "Known for its free-flowing play and passionate supporters.",
            "Its minimal equipment and universal appeal make it a worldwide favorite."
        ]
    },
    "basketball": {
        "vague": [
            "A dynamic game where the court becomes a stage.",
            "Often remembered for its fast breaks and soaring leaps.",
            "A sport that pulses with energy and split-second decisions."
        ],
        "helpful": [
            "It involves shooting a ball through a raised hoop.",
            "Known for its mix of individual flair and team coordination.",
            "Its fast-paced, high-scoring nature captivates audiences."
        ]
    },
    "tennis": {
        "vague": [
            "A game of finesse played on a neatly marked court.",
            "Often seen as a battle of endurance and precision.",
            "A sport where swift movements and sharp reflexes reign."
        ],
        "helpful": [
            "It involves hitting a small ball with a racket over a net.",
            "Known for its graceful footwork and competitive rallies.",
            "Its blend of power and strategy makes it an enduring favorite."
        ]
    },
    "baseball": {
        "vague": [
            "A time-honored game evoking nostalgic summer days.",
            "Often linked to leisurely afternoons and community cheers.",
            "A sport that unfolds on a diamond of dreams."
        ],
        "helpful": [
            "It involves hitting a pitched ball and running around bases.",
            "Known for its rich tradition and strategic play.",
            "Its slow pace mixed with moments of brilliance makes it unique."
        ]
    },
    "golf": {
        "vague": [
            "A quiet pursuit played on sprawling, manicured greens.",
            "Often viewed as a test of precision under calm skies.",
            "A sport where every swing is a measured act of focus."
        ],
        "helpful": [
            "It involves driving a ball into a series of holes with minimal strokes.",
            "Known for its serene courses and emphasis on accuracy.",
            "Its blend of patience and skill appeals to many."
        ]
    },
    "boxing": {
        "vague": [
            "A combat sport that pits agility against sheer will.",
            "Often associated with raw power and endurance.",
            "A contest where every punch tells a story."
        ],
        "helpful": [
            "It involves two opponents exchanging blows in a ring.",
            "Known for its strategic footwork and explosive action.",
            "Its intensity and focus make it a test of grit."
        ]
    },
    "cricket": {
        "vague": [
            "A bat-and-ball game with a leisurely yet strategic pace.",
            "Often linked with long, sunlit days and tactical play.",
            "A sport that unfolds slowly with moments of brilliance."
        ],
        "helpful": [
            "It involves batting, bowling, and fielding in a carefully timed match.",
            "Known for its intricate rules and deep-rooted traditions.",
            "Its blend of patience and strategy captivates its fans."
        ]
    },
    "swimming": {
        "vague": [
            "A sport where fluid motion meets cool refreshment.",
            "Often seen as a graceful race against time and water.",
            "A challenge that tests both speed and endurance in liquid form."
        ],
        "helpful": [
            "It involves racing across water in pools or open water.",
            "Known for its emphasis on streamlined form and stamina.",
            "Its clean, rhythmic strokes define the essence of the sport."
        ]
    },
    "cycling": {
        "vague": [
            "A journey on two wheels through winding paths.",
            "Often linked with adventure and scenic escapades.",
            "A sport that blends speed with the beauty of nature."
        ],
        "helpful": [
            "It involves pedaling through various terrains with determination.",
            "Known for its balance of power, endurance, and technique.",
            "Its competitive and recreational forms both capture hearts."
        ]
    },
    "volleyball": {
        "vague": [
            "A high-energy game played with a bouncing ball and soaring leaps.",
            "Often seen as a contest of quick reflexes and smooth teamwork.",
            "A sport where every set and spike creates a lively rhythm."
        ],
        "helpful": [
            "It involves keeping a ball in the air by passing it over a net.",
            "Known for its fast-paced rallies and coordinated plays.",
            "Its mix of athleticism and strategy makes it a crowd favorite."
        ]
    },

    # Jobs
    "teacher": {
        "vague": [
            "A guide in a world of endless questions.",
            "Often seen as a mentor in a bustling classroom.",
            "A role that sparks curiosity without giving all the answers."
        ],
        "helpful": [
            "It involves sharing knowledge and inspiring new ideas.",
            "Known for nurturing minds and igniting creativity.",
            "Its impact is measured by the spark it lights in learners."
        ]
    },
    "doctor": {
        "vague": [
            "A healer who works behind the scenes of wellness.",
            "Often pictured in a realm of care and constant motion.",
            "A figure who mends bodies with a touch of mystery."
        ],
        "helpful": [
            "It involves diagnosing ailments and providing remedies.",
            "Known for a blend of science, compassion, and steady hands.",
            "Its practice is crucial for restoring health and hope."
        ]
    },
    "engineer": {
        "vague": [
            "A creator who turns abstract ideas into tangible designs.",
            "Often associated with innovation and clever fixes.",
            "A mind that constructs solutions out of thin air."
        ],
        "helpful": [
            "It involves designing systems and solving technical puzzles.",
            "Known for analytical skills and a practical approach.",
            "Its work builds the foundation of modern conveniences."
        ]
    },
    "chef": {
        "vague": [
            "A culinary wizard blending flavors into art.",
            "Often seen as a master of secret recipes.",
            "A creative force behind every delicious dish."
        ],
        "helpful": [
            "It involves preparing meals that delight both taste and sight.",
            "Known for combining ingredients into memorable flavors.",
            "Its expertise transforms everyday food into experiences."
        ]
    },
    "artist": {
        "vague": [
            "A dreamer who paints the world in unique colors.",
            "Often lost in creative reverie and vibrant visions.",
            "A soul whose work speaks in subtle, unexpected ways."
        ],
        "helpful": [
            "It involves expressing ideas through visual or auditory media.",
            "Known for a perspective that sees beauty in the mundane.",
            "Its creations evoke emotions without spelling everything out."
        ]
    },
    "pilot": {
        "vague": [
            "A navigator of skies filled with endless blue.",
            "Often pictured as a free spirit riding on clouds.",
            "A person who turns the horizon into a playground."
        ],
        "helpful": [
            "It involves steering aircraft and ensuring safe journeys.",
            "Known for precise skills and calm decision-making under pressure.",
            "Its role keeps travelers aloft and on schedule."
        ]
    },
    "nurse": {
        "vague": [
            "A caring presence in the midst of life’s urgencies.",
            "Often seen as a comforting figure in bustling wards.",
            "A guardian of health whose touch eases pain."
        ],
        "helpful": [
            "It involves providing essential care and emotional support.",
            "Known for its empathy and critical role in patient recovery.",
            "Its work is a blend of medical skill and compassionate care."
        ]
    },
    "firefighter": {
        "vague": [
            "A brave soul who rushes toward danger in silence.",
            "Often seen as a beacon of hope amidst chaos.",
            "A guardian who faces fire with steadfast resolve."
        ],
        "helpful": [
            "It involves battling blazes and rescuing those in peril.",
            "Known for quick reflexes and unyielding courage.",
            "Its duty is to protect life and property under extreme conditions."
        ]
    },
    "police": {
        "vague": [
            "A vigilant presence that maintains order in the streets.",
            "Often seen as a silent guardian of community peace.",
            "A figure whose role is wrapped in duty and resolve."
        ],
        "helpful": [
            "It involves enforcing laws and ensuring public safety.",
            "Known for its constant vigilance and commitment to justice.",
            "Its presence helps keep neighborhoods safe and orderly."
        ]
    },
    "musician": {
        "vague": [
            "A creator who breathes life into sound and rhythm.",
            "Often seen as a storyteller without uttering words.",
            "A soul who transforms silence into moving melodies."
        ],
        "helpful": [
            "It involves composing or performing music that stirs the heart.",
            "Known for a passion that resonates in every note.",
            "Its craft turns everyday sounds into an art form."
        ]
    },

    # Vehicles (New)
    "car": {
        "vague": [
            "A common mode of modern transportation.",
            "Often seen cruising down highways.",
            "A compact machine built for speed and comfort."
        ],
        "helpful": [
            "It typically has four wheels and an engine.",
            "Used for daily commuting and road trips.",
            "Its design balances performance with practicality."
        ]
    },
    "bicycle": {
        "vague": [
            "A two-wheeled vehicle powered by human effort.",
            "Often a symbol of eco-friendly travel.",
            "A simple machine that blends fitness and freedom."
        ],
        "helpful": [
            "It has pedals and a chain mechanism.",
            "Used for commuting and leisurely rides.",
            "Its design is lightweight and efficient."
        ]
    },
    "airplane": {
        "vague": [
            "A soaring machine that defies gravity.",
            "Often associated with long journeys and high altitudes.",
            "A vehicle that carries people across continents."
        ],
        "helpful": [
            "It has wings, engines, and a fuselage.",
            "Used for fast, long-distance travel.",
            "Its design focuses on aerodynamics and speed."
        ]
    },
    "train": {
        "vague": [
            "A long, connected series of vehicles on tracks.",
            "Often seen as a symbol of industrial progress.",
            "A mode of transport that weaves through landscapes."
        ],
        "helpful": [
            "It is powered by diesel, electricity, or steam.",
            "Used for both commuter and long-distance travel.",
            "Its cars connect to form a single, efficient system."
        ]
    },
    "boat": {
        "vague": [
            "A vessel that moves gracefully on water.",
            "Often associated with leisure and adventure.",
            "A means of travel on lakes, rivers, or seas."
        ],
        "helpful": [
            "It is designed to float and navigate waterways.",
            "Used for fishing, cruising, or competitive sailing.",
            "Its design prioritizes buoyancy and balance."
        ]
    },
    "motorcycle": {
        "vague": [
            "A two-wheeled motor vehicle known for its agility.",
            "Often linked to freedom on open roads.",
            "A compact machine that exudes cool energy."
        ],
        "helpful": [
            "It has an engine and is built for speed.",
            "Used for fast travel and spirited rides.",
            "Its design emphasizes maneuverability and style."
        ]
    },
    "bus": {
        "vague": [
            "A large vehicle designed to transport many people.",
            "Often a workhorse of urban transit.",
            "A common sight in public transportation."
        ],
        "helpful": [
            "It features multiple doors and ample seating.",
            "Used to shuttle crowds across cities.",
            "Its design focuses on capacity and efficiency."
        ]
    },
    "helicopter": {
        "vague": [
            "A rotorcraft that hovers and takes off vertically.",
            "Often associated with emergency services.",
            "A vehicle that can access remote or congested areas."
        ],
        "helpful": [
            "It uses rotors for lift and propulsion.",
            "Commonly deployed for rescues and aerial views.",
            "Its compact design makes it versatile in flight."
        ]
    },
    "submarine": {
        "vague": [
            "A vessel that delves beneath the waves.",
            "Often shrouded in deep-sea mystery.",
            "A machine that navigates the underwater realm."
        ],
        "helpful": [
            "It is built to operate under high water pressure.",
            "Used in military, research, and exploration.",
            "Its design allows it to submerge and resurface safely."
        ]
    },
    "truck": {
        "vague": [
            "A heavy-duty vehicle designed for hauling.",
            "Often seen transporting goods on highways.",
            "A robust machine built for carrying loads."
        ],
        "helpful": [
            "It has a large cargo area and a powerful engine.",
            "Essential in logistics and freight transport.",
            "Its design emphasizes strength and durability."
        ]
    },

    # Mythology (New)
    "zeus": {
        "vague": [
            "A powerful god ruling the skies.",
            "Often depicted wielding lightning.",
            "A figure of supreme authority in ancient lore."
        ],
        "helpful": [
            "King of the Greek gods, ruling over the heavens.",
            "Known for his thunderbolt and majestic presence.",
            "His domain includes the sky and weather."
        ]
    },
    "odin": {
        "vague": [
            "A wise, one-eyed deity shrouded in mystery.",
            "Often associated with sacrifice and wisdom.",
            "A powerful figure from Norse legends."
        ],
        "helpful": [
            "Chief of the Norse gods, seeking knowledge at all costs.",
            "Recognized for his one eye and his runic secrets.",
            "His symbols include ravens and a spear."
        ]
    },
    "anubis": {
        "vague": [
            "A guardian of the underworld in ancient tales.",
            "Often linked with mummification and death.",
            "A figure guiding souls to the afterlife."
        ],
        "helpful": [
            "Egyptian god associated with embalming and funerary rites.",
            "Recognized by his jackal head and protective role.",
            "He ensures safe passage for souls into the afterlife."
        ]
    },
    "poseidon": {
        "vague": [
            "A mighty god ruling the seas.",
            "Often depicted with a trident.",
            "A force of nature both calm and tempestuous."
        ],
        "helpful": [
            "Greek god of the sea, earthquakes, and horses.",
            "His trident controls the waves and storms.",
            "He is known for both his wrath and his benevolence."
        ]
    },
    "hades": {
        "vague": [
            "A mysterious ruler of the realm of the dead.",
            "Often depicted in dark, somber tones.",
            "A figure whose domain is the underworld."
        ],
        "helpful": [
            "Greek god of the underworld, overseeing the dead.",
            "Known for his solemn, grim authority.",
            "His presence reminds mortals of life's impermanence."
        ]
    },
    "thor": {
        "vague": [
            "A thunderous god wielding a mighty hammer.",
            "Often portrayed as a fierce protector.",
            "A warrior deity with a stormy presence."
        ],
        "helpful": [
            "Norse god of thunder, famous for his hammer Mjölnir.",
            "Celebrated for his strength and heroic deeds.",
            "His battles are the stuff of legend."
        ]
    },
    "ares": {
        "vague": [
            "A fierce deity embodying the chaos of battle.",
            "Often depicted amid the clamor of war.",
            "A symbol of raw, unbridled aggression."
        ],
        "helpful": [
            "Greek god of war, representing conflict and strife.",
            "Known for his temper and martial prowess.",
            "His influence is felt on battlefields."
        ]
    },
    "isis": {
        "vague": [
            "A nurturing goddess revered for her magic.",
            "Often associated with healing and protection.",
            "A figure of ancient wisdom and fertility."
        ],
        "helpful": [
            "Egyptian goddess known for her restorative powers.",
            "Celebrated for her role as a mother and healer.",
            "Her mythology centers on protection and rebirth."
        ]
    },
    "kraken": {
        "vague": [
            "A legendary sea monster of immense size.",
            "Often whispered about in sailor's tales.",
            "A creature of myth lurking in the deep."
        ],
        "helpful": [
            "A fabled beast said to have massive tentacles.",
            "Known for causing terror in ancient maritime lore.",
            "Its myth represents the mystery of the ocean depths."
        ]
    },
    "phoenix": {
        "vague": [
            "A mythical bird reborn from its ashes.",
            "Often associated with fire and renewal.",
            "A symbol of eternal rebirth and hope."
        ],
        "helpful": [
            "A legendary creature that cyclically regenerates.",
            "Its flames consume the old to bring forth the new.",
            "It stands as a metaphor for transformation and immortality."
        ]
    },

    # Technology (New)
    "computer": {
        "vague": [
            "A modern marvel that processes vast data.",
            "Often seen as the heart of digital innovation.",
            "A device that transforms information into power."
        ],
        "helpful": [
            "It executes programs and performs complex calculations.",
            "An essential tool in modern work and play.",
            "Its evolution has revolutionized global communication."
        ]
    },
    "smartphone": {
        "vague": [
            "A compact device connecting you to the world.",
            "Often a symbol of modern communication.",
            "A gadget that fits in your pocket yet spans the globe."
        ],
        "helpful": [
            "It combines telephony with powerful computing.",
            "A personal assistant, camera, and communicator in one.",
            "Its interface has transformed how we interact with technology."
        ]
    },
    "robot": {
        "vague": [
            "A mechanical being programmed to serve.",
            "Often depicted in futuristic visions.",
            "A creation that blurs the line between man and machine."
        ],
        "helpful": [
            "It automates tasks and can perform repetitive actions.",
            "Used in industries from manufacturing to exploration.",
            "Its development continues to shape the future of work."
        ]
    },
    "drone": {
        "vague": [
            "A flying machine that operates without a pilot.",
            "Often seen capturing aerial views.",
            "A device that hovers above with silent precision."
        ],
        "helpful": [
            "It is used for photography, surveillance, and delivery.",
            "Operated remotely or autonomously for various tasks.",
            "Its compact design enables agile flight in tight spaces."
        ]
    },
    "satellite": {
        "vague": [
            "A silent guardian orbiting the Earth.",
            "Often linked with global communications.",
            "A machine that watches over from space."
        ],
        "helpful": [
            "It relays signals for weather, navigation, and data.",
            "An essential component of modern telecommunications.",
            "Its orbit ensures continuous coverage of the planet."
        ]
    },
    "internet": {
        "vague": [
            "An invisible web that connects the world.",
            "Often described as a digital ecosystem.",
            "A realm where information flows without borders."
        ],
        "helpful": [
            "It enables global connectivity and communication.",
            "Used for social interaction, business, and entertainment.",
            "Its infrastructure is the backbone of the modern world."
        ]
    },
    "server": {
        "vague": [
            "A robust machine that stores and serves data.",
            "Often hidden in massive data centers.",
            "A workhorse of the digital age."
        ],
        "helpful": [
            "It processes requests and delivers information.",
            "Crucial for hosting websites, apps, and services.",
            "Its performance is key to online experiences."
        ]
    },
    "algorithm": {
        "vague": [
            "A set of instructions that solves problems step by step.",
            "Often hidden behind the magic of computation.",
            "A blueprint for decision-making in code."
        ],
        "helpful": [
            "It provides a systematic method to solve tasks.",
            "Used in everything from search engines to recommendation systems.",
            "Its efficiency can be a game-changer in software performance."
        ]
    },
    "database": {
        "vague": [
            "A structured repository of organized information.",
            "Often considered the backbone of data-driven systems.",
            "A digital vault where data is carefully stored."
        ],
        "helpful": [
            "It efficiently stores and retrieves large volumes of data.",
            "Critical for applications ranging from banking to social media.",
            "Its structure is key to managing and accessing information."
        ]
    },
    "chip": {
        "vague": [
            "A tiny component that powers modern electronics.",
            "Often called the brain of digital devices.",
            "A micro marvel that enables complex computing."
        ],
        "helpful": [
            "It performs millions of calculations per second.",
            "Essential for smartphones, computers, and appliances.",
            "Its miniaturization is a cornerstone of modern technology."
        ]
    },

    # Languages (New)
    "english": {
        "vague": [
            "A global language of literature and commerce.",
            "Often a bridge between diverse cultures.",
            "A language known for its flexibility and reach."
        ],
        "helpful": [
            "It is widely used as a common language worldwide.",
            "Its vocabulary is vast and continually evolving.",
            "Its influence is seen in media, business, and education."
        ]
    },
    "spanish": {
        "vague": [
            "A language with a rhythmic and passionate sound.",
            "Often linked to vibrant cultures and lively conversation.",
            "A tongue that dances with emotion and flair."
        ],
        "helpful": [
            "It is spoken by millions across the globe.",
            "Known for its expressive intonation and regional diversity.",
            "Its literature and music are rich with history and passion."
        ]
    },
    "french": {
        "vague": [
            "A language synonymous with romance and art.",
            "Often admired for its elegance and charm.",
            "A tongue that flows like poetry."
        ],
        "helpful": [
            "It is considered a language of culture and diplomacy.",
            "Famous for its contributions to art, cuisine, and fashion.",
            "Its refined pronunciation and style are celebrated."
        ]
    },
    "mandarin": {
        "vague": [
            "A tonal language steeped in ancient tradition.",
            "Often seen as the language of a vast empire.",
            "A language where each character tells a story."
        ],
        "helpful": [
            "It is the most spoken language in the world.",
            "Known for its logographic writing system.",
            "Its tonal nature and characters make it uniquely challenging."
        ]
    },
    "arabic": {
        "vague": [
            "A language rich in poetry and historical depth.",
            "Often resonating with a rhythmic cadence.",
            "A tongue that carries centuries of legacy."
        ],
        "helpful": [
            "It is widely spoken in the Middle East and North Africa.",
            "Famous for its beautiful calligraphy and expressive vocabulary.",
            "Its grammar and script have influenced many cultures."
        ]
    },
    "hindi": {
        "vague": [
            "A vibrant language spoken by millions.",
            "Often filled with expressive intonation and warmth.",
            "A language that intertwines tradition with modernity."
        ],
        "helpful": [
            "It is one of the official languages of India.",
            "Known for its poetic expression and rich heritage.",
            "Its script and sounds reflect a diverse cultural tapestry."
        ]
    },
    "russian": {
        "vague": [
            "A language of deep literature and powerful emotion.",
            "Often described as robust and resonant.",
            "A tongue that carries the weight of history."
        ],
        "helpful": [
            "It is the most widely spoken Slavic language.",
            "Noted for its complex grammar and expressive vocabulary.",
            "Its literary tradition is renowned across the globe."
        ]
    },
    "portuguese": {
        "vague": [
            "A melodic language with a soulful cadence.",
            "Often linked to seafaring adventures and warm cultures.",
            "A language spoken across continents with charm."
        ],
        "helpful": [
            "It is the official language of Portugal and Brazil.",
            "Known for its lyrical intonation and expressive style.",
            "Its influence is felt in music, art, and literature."
        ]
    },
    "japanese": {
        "vague": [
            "A language where tradition meets modernity.",
            "Often noted for its politeness and precision.",
            "A tongue with a unique blend of elegance and formality."
        ],
        "helpful": [
            "It employs kanji along with two syllabaries.",
            "Known for its succinct expressions and rich culture.",
            "Its writing system and grammar offer a distinct charm."
        ]
    },
    "german": {
        "vague": [
            "A language known for its precision and structure.",
            "Often characterized by its compound words and clarity.",
            "A tongue that exudes strength and order."
        ],
        "helpful": [
            "It is widely used in science, engineering, and philosophy.",
            "Noted for its systematic grammar and extensive vocabulary.",
            "Its literary and cultural contributions are globally significant."
        ]
    }
}

"""
Metadata and agricultural treatment guides for the 38 PlantVillage classes.
"""

CLASS_NAMES = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Blueberry___healthy',
    'Cherry_(including_sour)___Powdery_mildew',
    'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Peach___Bacterial_spot',
    'Peach___healthy',
    'Pepper,_bell___Bacterial_spot',
    'Pepper,_bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Raspberry___healthy',
    'Soybean___healthy',
    'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch',
    'Strawberry___healthy',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

CLASS_DETAILS = {
    'Apple___Apple_scab': {
        'plant': 'Apple',
        'condition': 'Apple Scab',
        'status': 'Diseased',
        'cause': 'Fungus (Venturia inaequalis)',
        'description': 'Produces dull olive-green to velvety brown-black lesions on leaves and fruit, causing yellowing and defoliation.',
        'treatment': 'Apply preventative fungicides (captan, sulfur, or myclobutanil) early in spring. Rake and destroy fallen leaves in autumn to eliminate overwintering spores.'
    },
    'Apple___Black_rot': {
        'plant': 'Apple',
        'condition': 'Black Rot (Frogeye Leaf Spot)',
        'status': 'Diseased',
        'cause': 'Fungus (Diplodia seriata)',
        'description': 'Circular brown spots with distinct purple borders on foliage; can lead to fruit rot and cankers on branches.',
        'treatment': 'Prune dead or diseased limbs during dormant periods. Apply protectant copper or captan sprays before blossom opening.'
    },
    'Apple___Cedar_apple_rust': {
        'plant': 'Apple',
        'condition': 'Cedar Apple Rust',
        'status': 'Diseased',
        'cause': 'Fungus (Gymnosporangium juniperi-virginianae)',
        'description': 'Yellow-orange spots with swollen centers on leaf surfaces, later developing small tube-like structures on undersides.',
        'treatment': 'Remove nearby Eastern Red Cedar hosts within 1-2 miles if possible. Apply preventative fungicides during spring leaf emergence.'
    },
    'Apple___healthy': {
        'plant': 'Apple',
        'condition': 'Healthy Apple Foliage',
        'status': 'Healthy',
        'cause': 'None (Plant is healthy)',
        'description': 'Clean, vibrant green apple foliage exhibiting normal growth without fungal or bacterial symptoms.',
        'treatment': 'Maintain routine orchard scouting, proper pruning for sunlight penetration, and balanced irrigation.'
    },
    'Blueberry___healthy': {
        'plant': 'Blueberry',
        'condition': 'Healthy Blueberry Foliage',
        'status': 'Healthy',
        'cause': 'None (Plant is healthy)',
        'description': 'Uniform deep green blueberry leaves showing vigorous vegetative development.',
        'treatment': 'Maintain acidic soil pH (4.5–5.5), apply pine needle or bark mulch, and irrigate regularly.'
    },
    'Cherry_(including_sour)___Powdery_mildew': {
        'plant': 'Cherry',
        'condition': 'Powdery Mildew',
        'status': 'Diseased',
        'cause': 'Fungus (Podosphaera clandestina)',
        'description': 'White powdery fungal coating on young leaves and terminal shoots, leading to curled, distorted foliage.',
        'treatment': 'Prune interior canopy for sunlight and air flow. Apply potassium bicarbonate, horticultural oils, or sulfur-based sprays.'
    },
    'Cherry_(including_sour)___healthy': {
        'plant': 'Cherry',
        'condition': 'Healthy Cherry Foliage',
        'status': 'Healthy',
        'cause': 'None (Plant is healthy)',
        'description': 'Vibrant cherry leaves with smooth margins and no signs of mildew, spots, or pest injury.',
        'treatment': 'Standard orchard management, dormant oil application in late winter, and scheduled seasonal nutrition.'
    },
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': {
        'plant': 'Corn (Maize)',
        'condition': 'Cercospora Gray Leaf Spot',
        'status': 'Diseased',
        'cause': 'Fungus (Cercospora zeae-maydis)',
        'description': 'Narrow rectangular lesions bounded by veins, turning tan or gray and coalescing across leaf blades.',
        'treatment': 'Plant tolerant corn hybrids, rotate crops away from corn for at least 1-2 seasons, and apply strobilurin/triazole fungicides if threshold reached.'
    },
    'Corn_(maize)___Common_rust_': {
        'plant': 'Corn (Maize)',
        'condition': 'Common Rust',
        'status': 'Diseased',
        'cause': 'Fungus (Puccinia sorghi)',
        'description': 'Golden brown to cinnamon-red powdery pustules scattered across both upper and lower leaf surfaces.',
        'treatment': 'Plant rust-resistant hybrids. Fungicides are rarely needed unless pustules appear heavily before tassel emergence.'
    },
    'Corn_(maize)___Northern_Leaf_Blight': {
        'plant': 'Corn (Maize)',
        'condition': 'Northern Leaf Blight',
        'status': 'Diseased',
        'cause': 'Fungus (Exserohilum turcicum)',
        'description': 'Elongate, cigar-shaped grayish-green or tan lesions spreading along leaf veins.',
        'treatment': 'Select resistant corn varieties, manage residue through conservation tillage, and apply preventative fungicides under high humidity.'
    },
    'Corn_(maize)___healthy': {
        'plant': 'Corn (Maize)',
        'condition': 'Healthy Corn Foliage',
        'status': 'Healthy',
        'cause': 'None (Plant is healthy)',
        'description': 'Lush, dark green maize foliage showing robust vegetative vigor and photosynthetic capacity.',
        'treatment': 'Ensure balanced nitrogen and potassium levels, scout for armyworms, and maintain proper soil moisture.'
    },
    'Grape___Black_rot': {
        'plant': 'Grape',
        'condition': 'Black Rot',
        'status': 'Diseased',
        'cause': 'Fungus (Guignardia bidwellii)',
        'description': 'Reddish-brown circular spots with dark borders on leaves; infected fruit shrivels into hard, black mummies.',
        'treatment': 'Remove mummified berries and infected canes during winter pruning. Apply mancozeb or myclobutanil from bud break through fruit set.'
    },
    'Grape___Esca_(Black_Measles)': {
        'plant': 'Grape',
        'condition': 'Esca (Black Measles)',
        'status': 'Diseased',
        'cause': 'Complex fungal trunk pathogen',
        'description': 'Interveinal yellowing and necrosis resembling "tiger stripes", often with dark speckling on berry skins.',
        'treatment': 'Prevent large pruning wounds during wet seasons. Protect cuts with wound sealants; replace severely debilitated vines.'
    },
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': {
        'plant': 'Grape',
        'condition': 'Leaf Blight (Isariopsis Leaf Spot)',
        'status': 'Diseased',
        'cause': 'Fungus (Pseudocercospora cladosporioides)',
        'description': 'Angular brown to black necrotic spots with yellowish margins on foliage, leading to early defoliation.',
        'treatment': 'Spray copper fungicides or broad-spectrum protectants. Improve trellis canopy ventilation.'
    },
    'Grape___healthy': {
        'plant': 'Grape',
        'condition': 'Healthy Grape Foliage',
        'status': 'Healthy',
        'cause': 'None (Plant is healthy)',
        'description': 'Strong grape leaves showing rich green color, unblemished surfaces, and balanced shoot growth.',
        'treatment': 'Maintain trellis airflow, thin crowded shoots, and monitor for powdery mildew early in the season.'
    },
    'Orange___Haunglongbing_(Citrus_greening)': {
        'plant': 'Citrus (Orange)',
        'condition': 'Citrus Greening (Huanglongbing)',
        'status': 'Diseased',
        'cause': 'Bacterium (Candidatus Liberibacter asiaticus)',
        'description': 'Asymmetric yellow mottling across veins, stunted growth, and small lopsided bitter fruits that remain green.',
        'treatment': 'Control the Asian citrus psyllid vector with systemic insecticides. Remove confirmed infected trees to protect surrounding orchards.'
    },
    'Peach___Bacterial_spot': {
        'plant': 'Peach',
        'condition': 'Bacterial Spot',
        'status': 'Diseased',
        'cause': 'Bacterium (Xanthomonas arboricola pv. pruni)',
        'description': 'Angular purple-brown lesions that dry up and fall out, giving leaves a perforated "shot-hole" look.',
        'treatment': 'Apply copper sprays during dormancy and early leaf bud. Plant resistant peach cultivars and avoid excessive nitrogen.'
    },
    'Peach___healthy': {
        'plant': 'Peach',
        'condition': 'Healthy Peach Foliage',
        'status': 'Healthy',
        'cause': 'None (Plant is healthy)',
        'description': 'Smooth, elongated peach leaves with vibrant green chlorophyll and no leaf curl or necrosis.',
        'treatment': 'Apply dormant copper spray before bud swell to prevent peach leaf curl; maintain open center canopy pruning.'
    },
    'Pepper,_bell___Bacterial_spot': {
        'plant': 'Bell Pepper',
        'condition': 'Bacterial Spot',
        'status': 'Diseased',
        'cause': 'Bacterium (Xanthomonas campestris pv. vesicatoria)',
        'description': 'Small circular yellow-green spots that become dark brown with water-soaked margins, leading to severe leaf drop.',
        'treatment': 'Use certified disease-free seed, avoid overhead sprinkler irrigation, and spray fixed copper combined with mancozeb.'
    },
    'Pepper,_bell___healthy': {
        'plant': 'Bell Pepper',
        'condition': 'Healthy Bell Pepper',
        'status': 'Healthy',
        'cause': 'None (Plant is healthy)',
        'description': 'Healthy pepper foliage with sturdy stems and glossy green leaf tissue.',
        'treatment': 'Provide steady irrigation, mulch to preserve moisture, and support heavy fruiting branches with stakes.'
    },
    'Potato___Early_blight': {
        'plant': 'Potato',
        'condition': 'Early Blight',
        'status': 'Diseased',
        'cause': 'Fungus (Alternaria solani)',
        'description': 'Dark brown spots featuring concentric target-like rings, usually beginning on older, lower foliage.',
        'treatment': 'Ensure balanced potassium and nitrogen. Apply chlorothalonil or copper-based fungicides when symptoms first appear.'
    },
    'Potato___Late_blight': {
        'plant': 'Potato',
        'condition': 'Late Blight',
        'status': 'Diseased',
        'cause': 'Oomycete (Phytophthora infestans)',
        'description': 'Fast-spreading irregular water-soaked pale green to dark brown lesions with white fuzz on leaf undersides in humid air.',
        'treatment': 'Destroy infected volunteer potato plants immediately. Apply systemic fungicides (metalaxyl/mancozeb) and avoid overhead watering.'
    },
    'Potato___healthy': {
        'plant': 'Potato',
        'condition': 'Healthy Potato Foliage',
        'status': 'Healthy',
        'cause': 'None (Plant is healthy)',
        'description': 'Strong, clean potato leaves without target rings, blights, or flea beetle damage.',
        'treatment': 'Hill soil around plants to prevent greening of tubers, monitor for blight during cool damp weather.'
    },
    'Raspberry___healthy': {
        'plant': 'Raspberry',
        'condition': 'Healthy Raspberry Foliage',
        'status': 'Healthy',
        'cause': 'None (Plant is healthy)',
        'description': 'Healthy compound raspberry leaves showing uniform green color and vigorous shoot elongation.',
        'treatment': 'Trellis canes for air penetration, prune out fruited floricanes post-harvest, and keep mulch fresh.'
    },
    'Soybean___healthy': {
        'plant': 'Soybean',
        'condition': 'Healthy Soybean Foliage',
        'status': 'Healthy',
        'cause': 'None (Plant is healthy)',
        'description': 'Healthy trifoliate soybean leaves indicating proper nitrogen fixation and vegetative vitality.',
        'treatment': 'Practice multi-year crop rotation, scout for soybean cyst nematode and aphids regularly.'
    },
    'Squash___Powdery_mildew': {
        'plant': 'Squash',
        'condition': 'Powdery Mildew',
        'status': 'Diseased',
        'cause': 'Fungus (Podosphaera xanthii)',
        'description': 'White powdery fungal spots spreading rapidly across upper and lower surfaces, turning leaves yellow and brittle.',
        'treatment': 'Space vines for ventilation. Apply potassium bicarbonate, organic neem oil, or sulfur early in the morning.'
    },
    'Strawberry___Leaf_scorch': {
        'plant': 'Strawberry',
        'condition': 'Leaf Scorch',
        'status': 'Diseased',
        'cause': 'Fungus (Diplocarpon earlianum)',
        'description': 'Small purple spots that enlarge and turn dark brown without white centers, giving leaves a scorched look.',
        'treatment': 'Mow and destroy infected foliage after renovation. Apply fungicides during flower bud development and runner growth.'
    },
    'Strawberry___healthy': {
        'plant': 'Strawberry',
        'condition': 'Healthy Strawberry Foliage',
        'status': 'Healthy',
        'cause': 'None (Plant is healthy)',
        'description': 'Clean, dark green trifoliate strawberry leaves showing strong root crown vigor.',
        'treatment': 'Use clean straw mulch to keep fruit off wet soil, utilize drip irrigation, and remove old runners.'
    },
    'Tomato___Bacterial_spot': {
        'plant': 'Tomato',
        'condition': 'Bacterial Spot',
        'status': 'Diseased',
        'cause': 'Bacterium (Xanthomonas spp.)',
        'description': 'Small dark water-soaked spots with yellow halos on foliage; leaves turn yellow and drop prematurely.',
        'treatment': 'Use pathogen-free seeds, avoid overhead watering, apply copper + mancozeb sprays, and rotate crops annually.'
    },
    'Tomato___Early_blight': {
        'plant': 'Tomato',
        'condition': 'Early Blight',
        'status': 'Diseased',
        'cause': 'Fungus (Alternaria linariae / solani)',
        'description': 'Concentric brown rings forming "bullseye" lesions on lower foliage, surrounded by chlorotic yellow halos.',
        'treatment': 'Prune lower foliage touching ground. Apply straw or plastic mulch. Spray copper or chlorothalonil preventative fungicides.'
    },
    'Tomato___Late_blight': {
        'plant': 'Tomato',
        'condition': 'Late Blight',
        'status': 'Diseased',
        'cause': 'Oomycete (Phytophthora infestans)',
        'description': 'Rapidly expanding water-soaked greasy gray-brown lesions with white fuzzy sporulation on leaf undersides.',
        'treatment': 'Remove and destroy heavily diseased plants immediately. Apply copper or systemic fungicides ahead of wet, cool weather.'
    },
    'Tomato___Leaf_Mold': {
        'plant': 'Tomato',
        'condition': 'Leaf Mold',
        'status': 'Diseased',
        'cause': 'Fungus (Passalora fulva)',
        'description': 'Pale greenish-yellow patches on upper leaf surfaces with olive-green velvety mold underneath.',
        'treatment': 'Increase greenhouse air ventilation, reduce relative humidity below 85%, and choose resistant tomato varieties.'
    },
    'Tomato___Septoria_leaf_spot': {
        'plant': 'Tomato',
        'condition': 'Septoria Leaf Spot',
        'status': 'Diseased',
        'cause': 'Fungus (Septoria lycopersici)',
        'description': 'Numerous small circular spots with dark margins and gray centers containing pinpoint black fruiting bodies.',
        'treatment': 'Avoid splashing soil onto lower leaves. Mulch heavily, sanitize stakes, and apply copper fungicides.'
    },
    'Tomato___Spider_mites Two-spotted_spider_mite': {
        'plant': 'Tomato',
        'condition': 'Two-Spotted Spider Mite Damage',
        'status': 'Diseased',
        'cause': 'Pest (Tetranychus urticae)',
        'description': 'Fine yellow speckling / stippling on leaves, followed by bronzing, drying, and fine webbing on leaf undersides.',
        'treatment': 'Spray with insecticidal soap, neem oil, or sulfur. Introduce predatory mites (Phytoseiulus persimilis) in greenhouses.'
    },
    'Tomato___Target_Spot': {
        'plant': 'Tomato',
        'condition': 'Target Spot',
        'status': 'Diseased',
        'cause': 'Fungus (Corynespora cassiicola)',
        'description': 'Brown pinpoint lesions enlarging into concentric target-like rings with yellow chlorotic halos.',
        'treatment': 'Improve plant spacing for airflow. Avoid overhead irrigation and apply protectant fungicides.'
    },
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': {
        'plant': 'Tomato',
        'condition': 'Tomato Yellow Leaf Curl Virus (TYLCV)',
        'status': 'Diseased',
        'cause': 'Begomovirus (vectored by Bemisia tabaci whiteflies)',
        'description': 'Severe upward curling and cupping of leaf margins, yellowing, and severe plant stunting with bushy appearance.',
        'treatment': 'Control whitefly populations with insect netting and yellow sticky traps. Plant TYLCV-resistant hybrids.'
    },
    'Tomato___Tomato_mosaic_virus': {
        'plant': 'Tomato',
        'condition': 'Tomato Mosaic Virus (ToMV)',
        'status': 'Diseased',
        'cause': 'Tobamovirus (mechanically transmitted via tools & hands)',
        'description': 'Mottled green and yellow mosaic patterns, blistered leaf texture, leaf narrowing, and stunted growth.',
        'treatment': 'Disinfect pruning shears with 20% nonfat dry milk or bleach. Remove and burn infected plants. Wash hands before handling.'
    },
    'Tomato___healthy': {
        'plant': 'Tomato',
        'condition': 'Healthy Tomato Foliage',
        'status': 'Healthy',
        'cause': 'None (Plant is healthy)',
        'description': 'Lush, dark green tomato leaves with sturdy stems and balanced vigor, free from spotting or viral mottling.',
        'treatment': 'Stake or cage vines, prune bottom foliage for ventilation, provide deep regular watering at soil level.'
    }
}

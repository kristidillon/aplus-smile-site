# -*- coding: utf-8 -*-
"""
Content model for the generated interior pages of www.aplusdentalfl.com.

Editing rules for whoever maintains this:
  * Every claim here must be verifiable by the practice. No awards, no
    outcome guarantees, no insurance-participation claims, no invented
    credentials or years of experience.
  * FAQs listed here are rendered as VISIBLE questions on the page. That is
    what makes the FAQPage structured data legitimate — never add an FAQ to
    this file that is not shown to a human reader.
  * Keep the Fort Lauderdale references natural. One in the H1, one or two
    in the body, and that is enough.
"""

SITE = "https://www.aplusdentalfl.com"

PRACTICE = {
    "name": "A+ Smile",
    "legal_name": "BNY Dental P.C.",
    "display": "A+ Smile / BNY Dental P.C.",
    "street": "6231 N Federal Hwy",
    "city": "Fort Lauderdale",
    "region": "FL",
    "zip": "33308",
    "phone_display": "(754) 802-1588",
    "phone_e164": "+17548021588",
    "urgent_display": "(347) 284-8463",
    "urgent_e164": "+13472848463",
    "email": "hello@aplusdentalfl.com",
    # Nearby municipalities genuinely served from a 33308 address on North
    # Federal Highway. Do not extend this list into "neighborhood pages".
    "area_served": [
        "Fort Lauderdale", "Oakland Park", "Wilton Manors",
        "Lauderdale-by-the-Sea", "Pompano Beach", "Sea Ranch Lakes",
        "Lighthouse Point",
    ],
}

DOCTORS = [
    {
        "slug": "dr-natalia-bartkova",
        "name": "Dr. Natalia Bartkova, DDS",
        "short": "Dr. Bartkova",
        "plain": "Natalia Bartkova",
        "honorific": "Dr.",
        "suffix": "DDS",
        "photo": "dr-bartkova.jpg",
        "meta": "General, restorative & cosmetic dentistry · NYU College of Dentistry",
        "focus": ["General dentistry", "Preventive care", "Restorative dentistry", "Cosmetic dentistry"],
        "alumni": "New York University College of Dentistry",
        "title": "Dr. Natalia Bartkova, DDS | Fort Lauderdale Dentist",
        "desc": "Meet Dr. Natalia Bartkova, DDS, a general, restorative and cosmetic dentist at A+ Smile on N Federal Hwy in Fort Lauderdale. Call (754) 802-1588.",
        "lede": "A general, restorative and cosmetic dentist who is known for slowing down — walking patients through every option in plain language before anything is decided.",
        "body": [
            ("How Dr. Bartkova practices", [
                "For Dr. Bartkova, an appointment is not finished until the patient understands it. She trained at New York University College of Dentistry and spent two decades practicing in New York City before joining A+ Smile in Fort Lauderdale, and she carries the same habit into every chair: explain the finding, show it on the screen, lay out the options, and let the patient choose without pressure.",
                "Her clinical philosophy is straightforward. A healthy smile starts with strong teeth and healthy gums — not just white ones. She would rather catch a hairline crack or early gum inflammation at a routine visit than rebuild a tooth a year later, which is why her exams tend to run long and her treatment plans tend to start small.",
            ]),
            ("What she treats", [
                "Dr. Bartkova handles the everyday backbone of the practice — comprehensive exams, cleanings and periodontal maintenance, fillings, crowns, and the cosmetic work that follows once the foundation is sound. Patients who describe themselves as anxious about dentistry are often referred to her chair on purpose.",
            ]),
        ],
        "faqs": [
            ("Is Dr. Bartkova taking new patients in Fort Lauderdale?",
             "Yes. A+ Smile is accepting new patients at the North Federal Highway office. Call (754) 802-1588 or email hello@aplusdentalfl.com and the office will help you find a time."),
            ("I get nervous at the dentist. How does she handle that?",
             "She goes slowly and explains each step before it happens, and nothing is started until you say you are ready. Tell the office when you book that you are anxious — it changes how the visit is scheduled and paced."),
        ],
    },
    {
        "slug": "dr-yuriy-kaziyev",
        "name": "Dr. Yuriy Kaziyev, DDS",
        "short": "Dr. Kaziyev",
        "plain": "Yuriy Kaziyev",
        "honorific": "Dr.",
        "suffix": "DDS",
        "photo": "dr-kaziyev.jpg",
        "meta": "Implant, restorative & cosmetic dentistry · NYU College of Dentistry",
        "focus": ["Dental implants", "Restorative dentistry", "Cosmetic dentistry", "Clear aligner treatment"],
        "alumni": "New York University College of Dentistry",
        "title": "Dr. Yuriy Kaziyev, DDS | Fort Lauderdale Implant Dentist",
        "desc": "Meet Dr. Yuriy Kaziyev, DDS, who places dental implants and plans restorative and cosmetic care at A+ Smile in Fort Lauderdale. Call (754) 802-1588.",
        "lede": "An implant and restorative dentist who plans the work digitally first — so the patient sees the finished result before treatment begins.",
        "body": [
            ("How Dr. Kaziyev practices", [
                "Dr. Kaziyev trained at New York University College of Dentistry and spent much of his career caring for families in Brooklyn before bringing his practice to Fort Lauderdale. He focuses on the treatment that changes how a smile both looks and works — implants, crowns, full-arch restorations, and clear aligner treatment.",
                "Nearly all of that work is planned digitally. Scans and imaging are used to map the case before an instrument is picked up, which keeps the surgical part shorter, the fit more precise, and the conversation with the patient concrete rather than hypothetical.",
            ]),
            ("What he treats", [
                "Single-tooth implants, multiple-tooth replacement, implant-supported dentures, crowns and bridges, veneers, and clear aligner treatment for adults and teens. He also sees a steady stream of second-opinion consultations from patients who have been quoted extensive work elsewhere and want a plain reading of what is actually necessary.",
            ]),
        ],
        "faqs": [
            ("Does Dr. Kaziyev place implants himself?",
             "Yes. Implant planning, placement, and the final restoration are handled in this office rather than split across referrals, so one doctor stays responsible for the result from start to finish."),
            ("Can I get a second opinion on a treatment plan from another office?",
             "Yes. Bring your imaging and the written plan if you have them. You will get a straight read on what is urgent, what can wait, and what is optional. Call (754) 802-1588 to arrange it."),
        ],
    },
]

SERVICES = [
    {
        "slug": "family-dentistry",
        "nav": "Family dentistry",
        "h1": "Family Dentistry in Fort Lauderdale",
        "service_type": "Family Dentistry",
        "title": "Family Dentist in Fort Lauderdale, FL | A+ Smile",
        "desc": "Family dentist in Fort Lauderdale seeing children, teens and adults at one North Federal Highway office. Same two doctors every visit. Call (754) 802-1588.",
        "card": "One office for the whole household — children, teens, adults and grandparents.",
        "lede": "One office for the whole household. Children, teens, adults and grandparents are seen by the same two doctors, so nobody in your family has to start over with a stranger.",
        "body": [
            ("Care that stays with a family over time", [
                "Most families in Fort Lauderdale end up scattered across three or four offices — a pediatric practice for the kids, a general dentist for the parents, a specialist somewhere else for the work nobody wanted. A+ Smile is built to be the single office instead.",
                "Dr. Natalia Bartkova and Dr. Yuriy Kaziyev see every patient personally. That continuity matters more than it sounds: when the same doctor has watched a molar for six years, a small change on this year's X-ray is obvious rather than debatable.",
            ]),
            ("What a family visit covers", [
                None,
                ["**Children and teens** — exams, cleanings, fluoride, sealants, and honest guidance on when orthodontic treatment is actually worth starting.",
                 "**Adults** — routine exams and cleanings, fillings, crowns, gum health monitoring, and night-guard therapy for grinding.",
                 "**Older adults** — restorative work, dentures and implant-supported options, and management of dry mouth and root decay.",
                 "**Everyone** — digital X-rays with low radiation exposure, and a written plan you can take home."],
            ]),
            ("Scheduling around a real week", [
                "Where the schedule allows, families are booked back to back so one trip up North Federal Highway covers several people. Tell the office who is coming when you call and they will try to group the appointments.",
            ]),
        ],
        "faqs": [
            ("At what age should a child first see a dentist?",
             "The American Dental Association recommends a first visit by the child's first birthday, or within six months of the first tooth appearing. Early visits are short and mostly about making the chair unremarkable."),
            ("Can our whole family be seen on the same day?",
             "Usually, yes. Mention everyone who needs an appointment when you call (754) 802-1588 and the office will try to build a single block rather than several separate trips."),
            ("Do you see teenagers and adults in the same practice?",
             "Yes. A+ Smile is a general family practice, so a teenager in aligners and a parent needing a crown are treated in the same office by the same two doctors."),
        ],
        "related": ["preventive-dentistry", "invisalign", "emergency-dentistry"],
    },
    {
        "slug": "preventive-dentistry",
        "nav": "Preventive dentistry",
        "h1": "Preventive Dentistry in Fort Lauderdale",
        "service_type": "Preventive Dentistry",
        "title": "Preventive Dentistry in Fort Lauderdale | A+ Smile",
        "desc": "Exams, cleanings, digital X-rays and oral cancer screening at A+ Smile in Fort Lauderdale. Keep small problems small. Call (754) 802-1588 to book.",
        "card": "Exams, cleanings, digital X-rays and screenings on a schedule that fits your life.",
        "lede": "The least expensive dentistry is the kind you do before anything hurts. Routine exams, cleanings, digital imaging and screenings, on a schedule built around your actual risk.",
        "body": [
            ("Why the routine visit earns its place", [
                "Cavities, cracks and gum disease are all quiet in their early stages. By the time a tooth is sensitive to cold or a gum bleeds every morning, the problem has usually been developing for months. A preventive visit exists to find those things while the fix is still small — a sealant instead of a filling, a filling instead of a crown, a deep cleaning instead of periodontal surgery.",
            ]),
            ("What is included in a preventive visit", [
                None,
                ["**Comprehensive exam** — every tooth, existing restorations, bite, jaw joint and soft tissue.",
                 "**Professional cleaning** — removal of the plaque and calculus that brushing cannot reach, above and just below the gumline.",
                 "**Digital X-rays** — lower radiation than film, and visible on screen immediately so you can see what the doctor sees.",
                 "**Periodontal measurement** — pocket depths charted so gum health can be tracked year over year rather than guessed at.",
                 "**Oral cancer screening** — a visual and physical check of the lips, tongue, floor of the mouth and throat.",
                 "**Fluoride or sealants** where they are indicated, most often for children and for adults with a history of decay."],
            ]),
            ("How often you actually need to come in", [
                "Twice a year is the common default, and it is right for many people. Patients with a history of gum disease, heavy tartar, dry mouth, diabetes, or who smoke are often better served every three to four months. That interval is a clinical decision made with you, not a scheduling policy.",
            ]),
        ],
        "faqs": [
            ("How often should I have my teeth cleaned?",
             "Every six months suits most patients. If you have a history of periodontal disease, build tartar quickly, smoke, or manage diabetes, the doctors may recommend a three- to four-month interval instead."),
            ("Are dental X-rays safe?",
             "The office uses digital sensors, which require significantly less radiation than traditional film. X-rays are taken only when there is a clinical reason, and existing images from another office can often be transferred instead of repeated."),
            ("My teeth do not hurt. Do I still need a checkup?",
             "Yes. Early decay, early gum disease and cracked teeth are usually painless. Pain tends to arrive at the point where treatment becomes larger and more expensive."),
        ],
        "related": ["periodontal-care", "family-dentistry", "restorative-dentistry"],
    },
    {
        "slug": "restorative-dentistry",
        "nav": "Restorative dentistry",
        "h1": "Restorative Dentistry in Fort Lauderdale",
        "service_type": "Restorative Dentistry",
        "title": "Restorative Dentist in Fort Lauderdale, FL | A+ Smile",
        "desc": "Fillings, crowns, bridges and full-mouth rehabilitation at A+ Smile in Fort Lauderdale. Repair damaged and worn teeth so they work again. Call (754) 802-1588.",
        "card": "Fillings, crowns, bridges and onlays that return a damaged tooth to full function.",
        "lede": "Repairing teeth that are cracked, decayed, worn down or already patched — so they hold up under a normal bite and stop being something you think about.",
        "body": [
            ("Restoring function first, appearance second", [
                "Restorative dentistry is the work that puts a tooth back to doing its job. Sometimes that is a single filling. Sometimes it is rebuilding a bite that has been collapsing for a decade under grinding or old failing restorations.",
                "The sequence at A+ Smile is deliberate: stabilize what is actively breaking down, restore function and a comfortable bite, and only then discuss cosmetic refinement. Cosmetic work built on an unstable foundation does not last, and rebuilding it twice is nobody's idea of value.",
            ]),
            ("Restorative options", [
                None,
                ["**Tooth-colored fillings** — composite that bonds to the tooth and is matched to its shade, for decay and small fractures.",
                 "**Inlays and onlays** — a conservative middle ground when a cavity is too large for a filling but the tooth does not need a full crown.",
                 "**Crowns** — full coverage for a tooth that is cracked, heavily filled, or has had root canal treatment.",
                 "**Bridges** — a fixed replacement for a missing tooth, anchored to the teeth on either side.",
                 "**Root canal treatment** — removing infected pulp so a tooth can be kept rather than extracted.",
                 "**Full-mouth rehabilitation** — staged reconstruction when wear, erosion or multiple failing restorations have changed the bite itself."],
            ]),
            ("What to expect", [
                None,
            ]),
        ],
        "steps": [
            ("Examination and imaging", "Digital X-rays and a full exam identify what is failing and why — decay, fracture, wear, or a bite problem driving all three."),
            ("A written plan, in order of urgency", "You get the sequence, not a single number: what needs treating now, what can be scheduled, and what is optional."),
            ("Treatment", "Work is grouped into as few appointments as is clinically sensible, so you are not returning eight times for eight teeth."),
            ("Bite check and follow-up", "The bite is verified after the restoration settles. A crown that is high by a fraction of a millimeter is a problem worth catching early."),
        ],
        "faqs": [
            ("How long does a crown last?",
             "With good hygiene and regular checkups, crowns commonly last well over a decade. Longevity depends on the health of the underlying tooth, your bite, and whether you grind — which is why a night guard is sometimes recommended alongside one."),
            ("Should I get a filling, an onlay, or a crown?",
             "It depends on how much healthy tooth structure is left. The doctors will show you the X-ray and the intraoral photo and explain where your tooth sits on that spectrum before you decide."),
            ("Can a badly damaged tooth be saved instead of extracted?",
             "Often, yes — with root canal treatment and a crown, or with a build-up and crown. Whether it is worth saving depends on the remaining structure and the health of the bone around it, and that is a conversation, not a formula."),
        ],
        "related": ["dental-implants", "cosmetic-dentistry", "preventive-dentistry"],
    },
    {
        "slug": "cosmetic-dentistry",
        "nav": "Cosmetic dentistry",
        "h1": "Cosmetic Dentistry in Fort Lauderdale",
        "service_type": "Cosmetic Dentistry",
        "title": "Cosmetic Dentist in Fort Lauderdale, FL | A+ Smile",
        "desc": "Veneers, bonding, whitening and smile design at A+ Smile in Fort Lauderdale. Results planned around your face, not a template. Call (754) 802-1588.",
        "card": "Veneers, bonding and smile design shaped around your face — not a template.",
        "lede": "Veneers, bonding, whitening and full smile design — planned around your face, your bite and your age, so the result reads as your smile rather than someone else's.",
        "body": [
            ("A smile that looks like it belongs to you", [
                "The failure mode in cosmetic dentistry is uniformity: identical, too-white, too-square teeth that announce themselves from across a room. Natural teeth are not identical. They have subtle variation in shade, translucency at the edges, and proportions that relate to the shape of the face they sit in.",
                "Dr. Kaziyev and Dr. Bartkova plan cosmetic cases around those relationships — lip line, midline, the curve of the smile against the lower lip, and how much tooth actually shows when you talk. The goal is a result nobody can point to.",
            ]),
            ("Cosmetic treatment offered", [
                None,
                ["**Porcelain veneers** — thin custom facings that correct shape, shade, chips and small gaps across the teeth that show.",
                 "**Composite bonding** — a same-visit, more conservative option for chips, small gaps and worn edges.",
                 "**Professional whitening** — in-office and take-home systems, covered in detail on the [teeth whitening](/services/teeth-whitening/) page.",
                 "**Tooth-colored restorations** — replacing dark or visible old fillings with bonded, shade-matched material.",
                 "**Gum contouring** — reshaping an uneven gumline or a smile that shows more gum than tooth.",
                 "**Clear aligner treatment** — often the better first move when crowding, not shape, is the real complaint."],
            ]),
            ("Planning before drilling", [
                "Cosmetic cases start with photographs, a scan and a conversation about what specifically bothers you — which is rarely what a dentist would guess. From there the doctors can show a planned result before treatment starts, so the design is agreed on while it is still easy to change.",
                "Complimentary cosmetic consultations are available. Call (754) 802-1588 to arrange one.",
            ]),
        ],
        "faqs": [
            ("How long do porcelain veneers last?",
             "Well-made porcelain veneers commonly last ten to fifteen years or more. Lifespan depends on your bite, whether you grind, and how well the gumline is maintained — the doctors will tell you honestly if grinding makes you a poor candidate."),
            ("Is bonding or are veneers right for me?",
             "Bonding is less expensive, done in a single visit, and reversible, but it stains and chips sooner. Veneers cost more and involve preparing the tooth, but hold their shade and shape far longer. The right answer depends on how many teeth are involved and how long you want the result to hold."),
            ("Will veneers look obviously fake?",
             "Not if they are designed well. Shade, translucency and proportion are chosen with you before anything is made, and you see the planned result first. Bring photos of smiles you like and photos of ones you do not — both are useful."),
            ("Do I need to fix my gums or bite first?",
             "Sometimes. Active gum disease, untreated decay or a collapsing bite will undermine cosmetic work, so those are addressed first. It is a longer path, but it is the one where the result survives."),
        ],
        "related": ["teeth-whitening", "invisalign", "restorative-dentistry"],
    },
    {
        "slug": "teeth-whitening",
        "nav": "Teeth whitening",
        "h1": "Teeth Whitening in Fort Lauderdale",
        "service_type": "Teeth Whitening",
        "title": "Teeth Whitening in Fort Lauderdale, FL | A+ Smile",
        "desc": "Professional in-office and take-home teeth whitening at A+ Smile in Fort Lauderdale, supervised by a dentist. Book a consult at (754) 802-1588.",
        "card": "In-office and custom take-home whitening, supervised so enamel and gums stay protected.",
        "lede": "Professional whitening, supervised by a dentist — stronger and more predictable than a drugstore kit, and applied with your enamel and gums actually protected.",
        "body": [
            ("Why supervised whitening is different", [
                "Over-the-counter strips use a low concentration of peroxide and a tray that fits nobody in particular. That combination is why results are uneven, why gel ends up on the gums, and why sensitivity is such a common complaint.",
                "Professional whitening uses a higher concentration under controlled conditions, with the gums isolated and a custom tray made from a scan of your own teeth. It also starts with an exam — because whitening an untreated cavity or a cracked tooth is a genuinely bad idea.",
            ]),
            ("Two ways to whiten", [
                None,
                ["**In-office whitening** — a single supervised appointment. The fastest route, and the usual choice before an event.",
                 "**Custom take-home trays** — trays made from a scan of your teeth, with professional-strength gel used over roughly one to two weeks at home. More gradual, easier on sensitive teeth, and reusable later for touch-ups.",
                 "**A combination** — an in-office session to set the shade, then trays to maintain it."],
            ]),
            ("What whitening will and will not change", [
                "Whitening works on natural tooth structure. It does not change the color of crowns, veneers, bonding or fillings — so if you have restorations in the smile line, the sequence matters: whiten first, then match the new restorations to the lighter shade.",
                "Some discoloration is internal rather than surface — from trauma, or from certain medications taken in childhood. Those cases usually respond better to bonding or veneers, and the doctors will say so at the consultation rather than after three rounds of gel.",
            ]),
        ],
        "faqs": [
            ("Does professional teeth whitening damage enamel?",
             "Used as directed and under supervision, professional whitening is not shown to damage enamel. Temporary sensitivity is the common side effect, and it typically resolves within a few days. Tell the doctors if your teeth are already sensitive — the protocol can be adjusted."),
            ("How long do the results last?",
             "Commonly one to two years, though it depends heavily on coffee, tea, red wine and smoking. Custom trays can be reused for occasional short touch-ups, which is why many patients prefer the take-home option."),
            ("Will whitening work on my crowns or veneers?",
             "No. Whitening gel only lightens natural tooth structure. If you have restorations in your smile line, whiten first and then match the replacements to your new shade."),
            ("Can I whiten if my teeth are sensitive?",
             "Usually. Sensitivity is managed with a lower-concentration gel, shorter wear times, or a desensitizing course beforehand. It is worth raising at the consultation so the plan starts in the right place."),
        ],
        "related": ["cosmetic-dentistry", "preventive-dentistry", "invisalign"],
    },
    {
        "slug": "dental-implants",
        "nav": "Dental implants",
        "h1": "Dental Implants in Fort Lauderdale",
        "service_type": "Dental Implants",
        "title": "Dental Implants in Fort Lauderdale, FL | A+ Smile",
        "desc": "Single-tooth, multiple-tooth and implant-supported denture options in Fort Lauderdale, planned digitally and placed in-office. Free consult — (754) 802-1588.",
        "card": "Single teeth or full arches, planned digitally and placed in this office.",
        "lede": "A replacement tooth that is anchored in bone rather than resting on it — planned digitally, placed in this office, and restored by the same doctor who planned it.",
        "body": [
            ("What a dental implant actually is", [
                "An implant is a small titanium post placed into the jawbone where a tooth root used to be. Over the following months the bone grows around it — a process called osseointegration — and once it is stable, a custom crown is attached on top.",
                "The reason implants are worth the time is what happens underneath. A missing tooth lets the jawbone in that area shrink, which changes the shape of the face and destabilizes the neighboring teeth. An implant is the only replacement that transmits chewing force into the bone the way a natural root does, which is what keeps the bone there.",
            ]),
            ("Implant options", [
                None,
                ["**Single-tooth implant** — one post, one crown. The neighboring teeth are left untouched, unlike a bridge.",
                 "**Multiple implants** — several posts supporting individual crowns or a short fixed bridge.",
                 "**Implant-supported dentures** — a denture that snaps onto implants instead of relying on suction and adhesive.",
                 "**Full-arch restoration** — a fixed set of teeth supported by several implants across an entire arch.",
                 "**Bone grafting** — building up the site first when a tooth has been missing long enough for the bone to recede."],
            ]),
            ("The implant process, step by step", [None]),
        ],
        "steps": [
            ("Consultation and 3D planning", "Imaging shows bone volume and the position of nerves and sinuses. The implant position is planned digitally before anything is scheduled."),
            ("Placement", "The post is placed under local anesthesia. Most patients describe it as more straightforward than the extraction that preceded it."),
            ("Healing", "Bone integrates with the implant over roughly three to six months, depending on the site and whether grafting was needed. A temporary tooth is usually provided in the meantime."),
            ("The final crown", "An impression or scan is taken and a custom crown is made and fitted — shaped and shaded to match the teeth beside it."),
        ],
        "body_after": [
            ("Are you a candidate?", [
                "Most healthy adults are. What matters most is enough bone to hold the implant and gums that are free of active infection — and both are addressable. Smoking, uncontrolled diabetes and some medications affect healing, which is why the medical history conversation is a real one rather than a form.",
                "Complimentary implant consultations are available at the Fort Lauderdale office, including honest pricing before you commit to anything. Call (754) 802-1588 to arrange one.",
            ]),
        ],
        "faqs": [
            ("How long does the dental implant process take?",
             "From placement to final crown is commonly three to six months, because the bone needs time to integrate with the implant. Cases that require bone grafting take longer. A temporary tooth is usually placed so you are not without one during healing."),
            ("Is getting an implant painful?",
             "Placement is done under local anesthesia, and most patients report less discomfort than they expected — often comparable to an extraction. Soreness for a few days afterward is normal and is typically managed with over-the-counter medication."),
            ("Am I too old for dental implants?",
             "There is no upper age limit. Bone quality and general health matter far more than age, and plenty of implant patients are in their seventies and eighties."),
            ("Implant or bridge — which is better for one missing tooth?",
             "An implant does not require cutting down the healthy teeth on either side, and it preserves the bone underneath. A bridge is faster and does not require surgery or a healing period. The doctors will walk through both against your specific situation."),
            ("What if I have been missing a tooth for years?",
             "That usually means some bone has been lost, but it rarely rules out an implant. Bone grafting can rebuild the site first. Imaging at the consultation will show exactly what you are working with."),
        ],
        "related": ["dentures", "restorative-dentistry", "periodontal-care"],
    },
    {
        "slug": "dentures",
        "nav": "Dentures",
        "h1": "Dentures in Fort Lauderdale",
        "service_type": "Dentures",
        "title": "Dentures in Fort Lauderdale, FL | A+ Smile",
        "desc": "Full, partial and implant-supported dentures at A+ Smile in Fort Lauderdale, fitted for comfort and a natural look. Call (754) 802-1588 to book a consult.",
        "card": "Full, partial and implant-supported dentures fitted for comfort and a natural look.",
        "lede": "Full, partial and implant-supported dentures — fitted properly, shaped to your face, and adjusted until they are something you stop noticing.",
        "body": [
            ("Modern dentures are not your grandparents' dentures", [
                "The reputation dentures carry — bulky, obviously artificial, prone to slipping — comes from materials and techniques that have moved on considerably. Today's are made from higher-quality acrylics and porcelains, designed from digital scans, and shaped to the individual face rather than a stock mold.",
                "Fit is where most of the difference lies, and fit is a process. The first set is a starting point; the adjustments over the following weeks are what turn it into something comfortable enough to forget about.",
            ]),
            ("Denture options", [
                None,
                ["**Complete dentures** — a full arch replacement, upper, lower or both.",
                 "**Partial dentures** — for patients who still have healthy natural teeth worth keeping, with the partial fitting around them.",
                 "**Implant-supported dentures** — a denture that snaps onto two or more [dental implants](/services/dental-implants/). Far more stable than a conventional denture, with no adhesive and no rocking while eating.",
                 "**Immediate dentures** — placed the same day teeth are removed so you are not without teeth during healing, then relined once the gums settle.",
                 "**Relines and repairs** — gums change shape over the years, and an existing denture can often be refitted rather than replaced."],
            ]),
            ("Living with a new denture", [
                "There is an adjustment period, and it is worth being honest about it. Speech takes a week or two to normalize. Eating starts with soft food and builds up. Minor sore spots are expected in the first weeks and are resolved with small adjustments — which is exactly why the follow-up appointments are part of the treatment rather than an afterthought.",
            ]),
        ],
        "faqs": [
            ("How long does it take to get used to new dentures?",
             "Most patients adjust over several weeks. Speech usually normalizes within one to two weeks, and eating confidence builds over a month or so. Sore spots in the early weeks are normal and are fixed with quick adjustments — do not wait them out."),
            ("Are implant-supported dentures worth the extra cost?",
             "For many patients, yes — particularly on the lower arch, where conventional dentures have the least suction to hold onto. They stay put while eating, require no adhesive, and help preserve jawbone. The consultation will lay out the difference against your situation."),
            ("Will dentures change how my face looks?",
             "A well-made denture supports the lips and cheeks, which often restores facial structure that was lost when teeth were removed. Tooth shape, size and shade are chosen with you, and photographs of your natural smile are genuinely useful to bring."),
            ("My current denture is loose. Do I need a new one?",
             "Not necessarily. Gums reshape over time, and a reline can often restore the fit of an otherwise sound denture. Bring it in and it can be assessed before anyone talks about replacing it."),
        ],
        "related": ["dental-implants", "restorative-dentistry", "periodontal-care"],
    },
    {
        "slug": "invisalign",
        "nav": "Invisalign & clear aligners",
        "h1": "Invisalign and Clear Aligners in Fort Lauderdale",
        "service_type": "Clear Aligner Orthodontic Treatment",
        "title": "Invisalign in Fort Lauderdale, FL | Clear Aligners | A+ Smile",
        "desc": "Invisalign and clear aligner treatment for adults and teens at A+ Smile in Fort Lauderdale, planned digitally start to finish. Call (754) 802-1588.",
        "card": "Clear aligner treatment for adults and teens, planned digitally from the first scan.",
        "lede": "Straightening teeth with a series of clear, removable aligners instead of fixed brackets and wires — planned digitally, so you see the projected result before you start.",
        "body": [
            ("How clear aligner treatment works", [
                "Treatment starts with a digital scan of your teeth. From that scan, the movement of each tooth is mapped out across the whole course of treatment, and a series of custom aligners is manufactured to carry out that plan a fraction of a millimeter at a time.",
                "Each aligner is worn about 20 to 22 hours a day and swapped for the next in the series roughly every one to two weeks. They come out to eat and to brush, which is the practical advantage over fixed braces: nothing is off-limits at dinner, and cleaning your teeth stays completely normal.",
            ]),
            ("What aligners treat well", [
                None,
                ["**Crowding** — teeth overlapping because there is not enough room in the arch.",
                 "**Spacing** — gaps between teeth, including a gap between the front two.",
                 "**Relapse after braces** — very common in adults who stopped wearing a retainer years ago.",
                 "**Mild to moderate bite issues** — overbite, underbite, crossbite and open bite within a certain range.",
                 "**Pre-restorative alignment** — moving teeth into better positions before veneers or crowns, so less tooth structure has to be removed."],
                "Severe skeletal bite discrepancies and complex rotations sometimes need fixed appliances or an orthodontic specialist. If your case is one of those, the doctors will tell you at the consultation rather than after you have paid for aligners.",
            ]),
            ("Adults and teens", [
                "Most aligner patients here are adults who did not want visible brackets at work, and teenagers who prefer aligners to braces. The requirement is the same for both: the aligners only work while they are actually in your mouth, so honest self-assessment about wear time is part of deciding whether this is the right treatment for you.",
            ]),
        ],
        "faqs": [
            ("How long does clear aligner treatment take?",
             "It depends on how far the teeth have to move. Minor corrections can finish in a few months; comprehensive cases commonly run twelve to eighteen months. You will get an estimate based on your own digital plan at the consultation, not a generic range."),
            ("Do I have to wear a retainer afterwards?",
             "Yes, and this is not optional. Teeth drift back toward their original positions without retention. Nightly retainer wear is what protects the result you paid for."),
            ("Are clear aligners really invisible?",
             "They are clear and close-fitting, so they are considerably less noticeable than metal brackets — but they are not literally invisible. Most people in conversation will not notice them; someone looking closely may."),
            ("Can I get aligners if I already had braces as a teenager?",
             "Very often, yes. Post-braces relapse is one of the most common reasons adults start aligner treatment, and those cases are frequently among the shorter ones."),
        ],
        "related": ["cosmetic-dentistry", "family-dentistry", "teeth-whitening"],
    },
    {
        "slug": "periodontal-care",
        "nav": "Periodontal care",
        "h1": "Periodontal Care in Fort Lauderdale",
        "service_type": "Periodontal Care",
        "title": "Periodontal & Gum Care in Fort Lauderdale, FL | A+ Smile",
        "desc": "Gum disease treatment in Fort Lauderdale — scaling and root planing, periodontal maintenance and bleeding-gum care at A+ Smile. Call (754) 802-1588.",
        "card": "Treatment for bleeding, receding and inflamed gums — the foundation everything else sits on.",
        "lede": "Bleeding gums are not normal, and gum disease is the leading reason adults lose teeth. Treated early, it is manageable — which is the entire argument for not ignoring it.",
        "body": [
            ("Gum disease is quiet until it is not", [
                "Periodontal disease begins as gingivitis: inflammation caused by bacteria at the gumline, showing up as redness, puffiness, and blood in the sink. At that stage it is reversible with professional cleaning and better home care.",
                "Left alone, the inflammation moves below the gumline and starts destroying the bone that holds teeth in place. That damage does not reverse on its own. Pockets deepen, gums recede, teeth loosen. The uncomfortable part is that it rarely hurts until it is advanced — which is why periodontal measurements are charted at every routine exam here rather than only when someone complains.",
            ]),
            ("Signs worth an appointment", [
                None,
                ["Gums that bleed when brushing or flossing",
                 "Persistent bad breath or a bad taste that does not clear",
                 "Gums that look red, swollen or tender",
                 "Teeth that appear longer as the gumline recedes",
                 "New sensitivity along the gumline",
                 "A tooth that feels loose, or a bite that suddenly feels different"],
            ]),
            ("How gum disease is treated", [
                None,
                ["**Scaling and root planing** — a deep cleaning that removes bacterial deposits from the root surfaces below the gumline and smooths them so the gums can reattach. Usually done with local anesthesia across one or two visits.",
                 "**Periodontal maintenance** — a cleaning interval of three to four months instead of six, which is what actually keeps treated periodontal disease stable long-term.",
                 "**Localized antimicrobial treatment** — placed directly into deeper pockets alongside cleaning where it is indicated.",
                 "**Referral to a periodontist** — for advanced cases needing surgical treatment or grafting. Knowing when to refer is part of treating this properly."],
            ]),
            ("Why it matters beyond your mouth", [
                "Periodontal disease is a chronic inflammatory condition, and research has consistently linked it with cardiovascular disease, diabetes and adverse pregnancy outcomes. The relationship is complex and still being studied, but there is no version of it where untreated chronic gum inflammation is a good idea.",
            ]),
        ],
        "faqs": [
            ("Is bleeding when I brush normal?",
             "No. Bleeding is a sign of inflammation, usually early gum disease. It is very treatable at that stage, so it is worth an appointment rather than a change of toothbrush."),
            ("What is the difference between a regular cleaning and a deep cleaning?",
             "A routine cleaning removes deposits at and just below the gumline. Scaling and root planing — a deep cleaning — goes further down the root surface to treat established pockets, and is usually done with local anesthesia."),
            ("Can gum disease be reversed?",
             "Gingivitis, the early stage, is reversible with treatment and consistent home care. Once bone has been lost to periodontitis, that bone does not come back on its own — but the disease can be stabilized and further loss prevented."),
            ("How often will I need cleanings after periodontal treatment?",
             "Most patients move to a three- or four-month periodontal maintenance interval. Pockets tend to repopulate with bacteria in roughly that window, which is why the shorter interval is what holds the result."),
        ],
        "related": ["preventive-dentistry", "dental-implants", "restorative-dentistry"],
    },
    {
        "slug": "emergency-dentistry",
        "nav": "Emergency dentistry",
        "h1": "Emergency Dentist in Fort Lauderdale",
        "service_type": "Emergency Dental Care",
        "title": "Emergency Dentist in Fort Lauderdale, FL | A+ Smile",
        "desc": "Dental emergency in Fort Lauderdale? Call A+ Smile at (754) 802-1588, or (347) 284-8463 for urgent care. Toothache, broken tooth, swelling and lost crowns.",
        "card": "Toothache, broken tooth, swelling or a lost crown — call and the office will get you seen.",
        "lede": "Toothache, a broken tooth, swelling, or a crown that came off at the worst possible time. Call the office and you will get a straight answer about how quickly you need to be seen.",
        "body": [
            ("Call first", [
                "**Office: (754) 802-1588. Urgent: (347) 284-8463.** Describing what happened over the phone lets the office triage it — some situations need an appointment within the hour, and some are safe to hold until tomorrow morning. Guessing at that on your own is the part that goes wrong.",
                "Go to a hospital emergency room instead if there is swelling that is spreading toward your eye or down your neck, if you have difficulty breathing or swallowing, if you have a high fever alongside dental pain, or if there is facial trauma involving a possible broken jaw.",
            ]),
            ("Common dental emergencies, and what to do first", [None]),
            ("What happens at an emergency visit", [
                "The first goal is getting you out of pain and controlling any infection. That may mean draining an abscess, starting antibiotics, placing a temporary restoration, or performing the emergency phase of root canal treatment.",
                "Definitive treatment usually follows at a scheduled appointment once the acute problem is settled. You will leave knowing what was done, what is still needed, and when.",
            ]),
        ],
        "emergency_list": [
            ("Severe toothache", "Rinse with warm salt water and use over-the-counter pain relief as directed. Do not hold aspirin against the gum — it burns the tissue. Persistent throbbing often means infection, so call."),
            ("Knocked-out permanent tooth", "Handle it by the crown, never the root. Rinse gently with milk or saline if dirty — do not scrub. Reinsert it into the socket if you can, or keep it in milk, and get to a dentist immediately. The first 30 to 60 minutes matter enormously."),
            ("Broken or chipped tooth", "Save any pieces and rinse your mouth with warm water. Use a cold compress outside the cheek for swelling. Call — a sharp edge can be smoothed the same day, and a deep fracture needs assessment quickly."),
            ("Lost filling or crown", "Keep the crown if you have it. Over-the-counter temporary cement can protect the tooth in the meantime. Avoid chewing on that side and call to have it recemented before the tooth shifts."),
            ("Facial swelling or a dental abscess", "This is the one to treat as urgent. Call immediately. Spreading swelling — especially toward the eye or down the neck — needs same-day care, and a hospital emergency room if it is progressing quickly."),
            ("Bleeding or injured gums and lips", "Apply firm pressure with clean gauze for 10 to 15 minutes. If bleeding does not slow, call the office or seek emergency care."),
        ],
        "faqs": [
            ("What counts as a dental emergency?",
             "Uncontrolled bleeding, facial swelling, a knocked-out permanent tooth, severe pain that is not responding to over-the-counter medication, and trauma to the mouth or jaw. When in doubt, call (754) 802-1588 and describe it — triage over the phone costs nothing."),
            ("What should I do with a knocked-out tooth?",
             "Pick it up by the crown, not the root. Rinse it gently with milk or saline if it is dirty, and either place it back in the socket or keep it submerged in milk. Get to a dentist immediately — the chance of saving the tooth drops sharply after the first hour."),
            ("Can a toothache go away on its own?",
             "Pain can fade when the nerve inside a tooth dies, and that is not recovery — the infection usually continues into the surrounding bone. A toothache that disappears without treatment still needs to be examined."),
            ("Should I go to the ER or a dentist?",
             "Go to an emergency room for facial trauma, difficulty breathing or swallowing, or swelling that is spreading. For toothache, broken teeth, lost restorations and localized infection, a dentist can treat the actual cause — an ER will generally only manage the pain."),
        ],
        "related": ["restorative-dentistry", "periodontal-care", "preventive-dentistry"],
    },
]

SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}

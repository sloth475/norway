
import pandas as pd
import re

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#stop = stopwords.words('english')

fh=open(r'datain.txt','r').read()
years=["years","yrs","yr","yo","Ys","ys"]

string = """
s:a 33 year old female crystallographer presents with mild spells of vertigo, mild headaches particularly at the back of the head and in the morning x 2 weeks. pt also reports chronic mild occasional lightheadedness. o:Height 160 cm, Weight 53.8 kg, Temperature 37.3 C, Pulse 76, SystolicBP 146, DiastolicBP 93, Respiration 15, Heart = 2/6 systolic murmur at base of heart, Chest = clear to auscultation B/L, no rales or wheezing, Extremities = no edema or clubbing, Heart = normal S1, S2, RRR a:Hypertension p:performed E/M Level 2 (established patient) - Completed, and prescribed Hydrochlorothiazide - 50 mg po qd, and ordered Cholesterol.


s:33 yr old female crystallographer presents today for routine exam. patient reports no acute problems. Patient reports that she never drinks alcohol. she denies smoking. o:Height 160 cm, Weight 53.8 kg, Temperature 37.3 C, Pulse 76, SystolicBP 146, DiastolicBP 93, Respiration 15, HPV I/H Risk DNA Probe negative for HPV 16 & 18, Visual Acuity Study right eye 20/20, left eye 20/20 a:normal exam. no current issues. problem status: Hypertension, being managed. administered immunization: FLUARIX p:Call office if any reaction from immunization. F/Up in one (1) year for annual check-up or sooner for new symptoms/problems as they arise.

s:a 32 year old f presents with critical dyspnea, critical shortness of breath and critical cough. Patient reports that she never drinks alcohol. patient has a one pack per day habit. o:Height 173 cm, Weight 91.1 kg, Temperature 37 C, Pulse 92, SystolicBP 142, DiastolicBP 91, Respiration 14, FEV1 FEV1=35 %, FEV1/FVC FEV1/FVC=60 %, Arterial Blood Gas PaCO2=44 mmHg,PaO2=58 mmHg, plum: accessory muscle use, Heart = RRR, Normal S1/S2, no murmurs, HEENT: WNL, rales Bil a:Chronic Obstructive Pulmonary Disease p:administered OMS 50 - 6 h via nasal cannula (contin), performed FEV1, FEV1/FVC, Arterial Blood Gas, and performed E/M Emergency Services Level 3 - Completed.
s:a white female aged 32 Ys presents with 8 months history of mild spells of vertigo. pt also reports increased frequency of mild ringing in the ears, mild headaches particularly at the back of the head and in the morning. o:Height 173 cm, Weight 93.2 kg, Temperature 37.1 C, Pulse 93, SystolicBP 147, DiastolicBP 94, Respiration 16, Heart = 2/6 systolic murmur at base of heart, Chest = clear to auscultation B/L, no rales or wheezing, Extremities = no edema or clubbing, Heart = normal S1, S2, RRR a:Hypertension p:performed E/M Level 2 (established patient) - Completed, and prescribed Hydrochlorothiazide - 50 mg po qd, and ordered Basic Metabolic Panel, Lipid panel.


s:32 yr old white F presents today for routine exam. pt reports no acute problems. she smokes 1 pack/day of cigarettes. she denies drinking alcohol.   o:Height 173 cm, Weight 92.2 kg, Temperature 37.1 C, Pulse 92, SystolicBP 145, DiastolicBP 92, Respiration 15, Pap smear no abnormal cervical cells, clinical breast exam no lumps noticed, Visual Acuity Study right eye 20/20, left eye 20/20, Pelvic exam uterus and ovaries are normal in size and location, valvula, cervix and vagina appears normal a:regular wellness visit. no complaints at this time. problem status: 1) Chronic Obstructive Pulmonary Disease, being managed 2) Hypertension, being managed. administered immunization: FLUARIX p:Call office if any reaction from immunization. F/Up in one (1) year for annual check-up or sooner for new symptoms/problems as they arise.

s:female landlord aged 32 yrs presents without complaints. patient denies any specific issues. o:, Skin cancer screening no abnormal skin or mole present a:no current issues p:performed Skin cancer screening.
s:53 year old female presents today for routine exam with history of severe shortness of breath. pt complains of severe fever, severe cough. she states she has never smoked a cigarette in her life. Patient is a moderate drinker. o:Height 151 cm, Weight 58.6 kg, Temperature 37.2 C, Pulse 83, SystolicBP 110, DiastolicBP 70, Respiration 15, HPV I/H Risk DNA Probe negative for HPV 16 & 18, clinical breast exam no lumps noticed, Visual Acuity Study right eye 20/20, left eye 20/20, Heart = RRR, Normal S1/S2, no murmurs, actively coughing with sputum production - dark yellow, Neck = no JVD a:normal health maintenance exam. Chronic Obstructive Pulmonary Disease. problem status: Pyelonephritis, being managed.  p:performed HPV I/H Risk DNA Probe, clinical breast exam, Visual Acuity Study, and performed Periodic comprehensive preventive medicine..., new patient; 40-64 years - Completed, and ordered High-sensitivity fecal occult blood test, Bilateral Mammography, Intraoccular Pressure, Skin cancer screening, Bone Density Scan (DXA), and referred patient to pulmonary disease.
s:a 53 yr old female with C/O severe fever for 9 days. pt also reports severe shortness of breath, severe cough. she denies smoking. describes drinking an average of 12 beers a week for about 3 years in her past. o:Height 151 cm, Weight 59.1 kg, Temperature 37.3 C, Pulse 84, SystolicBP 112, DiastolicBP 72, Respiration 16, Heart = RRR, Normal S1/S2, no murmurs, actively coughing with sputum production - dark yellow, Neck = no JVD a:Chronic Obstructive Pulmonary Disease p:performed E/M Level 3 (established patient) - Completed, and prescribed Prednisone - 20 mg orally, and ordered Bullectomy - right lung.


s:patient presents for exam. patient denies any issues. patient is a 53 yo white female maid. o:, High-sensitivity fecal occult blood test Negative, Bilateral Mammography no mass seen on B/L breast, Skin cancer screening no abnormal skin or mole present a:no current issues p:performed High-sensitivity fecal occult blood test, Bilateral Mammography, Skin cancer screening.
s:53 yo white f presents and denies any issues. o:, Intraoccular Pressure eye pressure = 14 mmHg a:no current issues p:performed Intraoccular Pressure.

s:pt presents with Hemorrhagic Stroke for more than 6 days. he is a 32 year old m fortune teller. o:Height 68 in, Weight 168 lbs, Temperature 98.6 F, Pulse 79, SystolicBP 108, DiastolicBP 67, Respiration 15 a:Hemorrhagic Stroke p:performed E/M Level 2 (established patient) - Completed, and prescribed protamine sulfate - 1 mg /90 units of heparin overdosage, and ordered CT Head, ECG.


s:33 yo M fortune teller presents for periodic physical. patient says he has no complaints today and no changes to PMH/PSH.  CAGE = 1/4. o:Height 68 in, Weight 166 lbs, Temperature 98.5 F, Pulse 79, SystolicBP 106, DiastolicBP 64, Respiration 14, Visual Acuity Study right eye 20/20, left eye 20/20, Testicular exam no lumps noted a:regular wellness visit. no current issues. problem status: 1) Type 1 Diabetes, being managed 2) Hemorrhagic Stroke, being managed. administered immunization: FLUARIX p:Call office if any reaction from immunization. F/Up in one (1) year for annual check-up or sooner for new symptoms/problems as they arise.

s:a M aged 33 Ys presents without specific complaints. pt denies any specific issues. o:, Skin cancer screening no abnormal skin or mole present a:no complaints at this time p:performed Skin cancer screening.
s:33 yr old male fortune teller presents with severe b/l foot pain, moderate parethesia in lower limbs. he has history of severe weight loss. Denies ever using tobacco. describes drinking an average of 12 drinks a week for about 3 years in his past. o:Height 68 in, Weight 168 lbs, Temperature 98.6 F, Pulse 79, SystolicBP 108, DiastolicBP 66, Respiration 15, rectal exam = normal, no masses found, Eyes = OD: 20/150, OU:20/100, normal pupillary reflex, DTRs: 2+ throughout, sensation = decreased pinprick sensation B/L lower extremity, appears in NAD, appropriate speech, Neuro = CN 2-12 intact, motor: 5/5 strength throughout, Extremities = B/L 2+ pitting edema throughout a:Type 1 Diabetes p:performed E/M Level 3 (established patient) - Completed, and referred patient to endocrinology.
s:33 year old m presents with severe b/l foot pain x 4 weeks. patient also complains of moderate parethesia in lower limbs, severe weight loss. o:Height 68 in, Weight 166 lbs, Temperature 98.5 F, Pulse 79, SystolicBP 106, DiastolicBP 64, Respiration 14, rectal exam = normal, no masses found, Eyes = OD: 20/150, OU:20/100, normal pupillary reflex, DTRs: 2+ throughout, sensation = decreased pinprick sensation B/L lower extremity, appears in NAD, appropriate speech, Neuro = CN 2-12 intact, motor: 5/5 strength throughout, Extremities = B/L 2+ pitting edema throughout a:Type 1 Diabetes p:performed E/M Level 3 (established patient) - Completed, and prescribed Potassium Chl - 25 meq po qd.

s:M aged 45 ys presents with 7 days history of mild headaches particularly at the back of the head and in the morning, mild ringing in the ears, mild occasional lightheadedness and Hypertension. Patient reports that he never drinks alcohol. Denies ever using tobacco. o:Height 180 cm, Weight 84 kg, Temperature 36.9 C, Pulse 83, SystolicBP 145, DiastolicBP 93, Respiration 16, Heart = 2/6 systolic murmur at base of heart, Chest = clear to auscultation B/L, no rales or wheezing, Extremities = no edema or clubbing, Heart = normal S1, S2, RRR a:Hypertension p:performed E/M Level 3 (new patient) - Completed, and prescribed nifedipine - 10 mg 3 x day, and ordered Cholesterol.

s:45 year old white male complains of Acute Renal Failure and other medical problems. NKDA. o:Height 180 cm, Weight 84 kg, Temperature 36.9 C, Pulse 83, SystolicBP 109, DiastolicBP 69, Respiration 16 a:Acute Renal Failure p:performed E/M Level 2 (established patient) - Completed, and prescribed Isotonic Saline (0.9%) - 10 mL/kg per dose, and ordered CT abdomen/pelvis.


s:46 year old white male negotiator presents today for wellness exam. pt reports that he has no new health issues. Patient does not smoke. Patient reports that he never drinks alcohol. o:Height 180 cm, Weight 82.7 kg, Temperature 36.8 C, Pulse 83, SystolicBP 142, DiastolicBP 91, Respiration 15, Visual Acuity Study right eye 20/20, left eye 20/20, Testicular exam no lumps noted a:normal exam. no current issues. problem status: 1) Hypertension, being managed 2) Acute Renal Failure, being managed. administered immunization: FLUARIX p:Call office if any reaction from immunization. F/Up in one (1) year for annual check-up or sooner for new symptoms/problems as they arise.
s:patient presents and denies any issues. pt is a 46 yr old white male negotiator. o:, Digital Rectal Exam no lump noted, Skin cancer screening no abnormal skin or mole present a:no complaints at this time p:performed Digital Rectal Exam, Skin cancer screening.

s:patient presents for exam. pt denies any issues. he is a 46 yo white male negotiator. o:, Intraoccular Pressure eye pressure = 14 mmHg a:no current issues p:performed Intraoccular Pressure.
s:white F aged 32 Ys presents today for wellness exam. patient reports that she has no new health issues. Patient is a moderate drinker. patient reports that she smokes once or twice daily.  CAGE = 1/4. o:Height 157 cm, Weight 44.8 kg, Temperature 37.2 C, Pulse 80, SystolicBP 111, DiastolicBP 72, Respiration 16, Pap smear no abnormal cervical cells, clinical breast exam no lumps noticed, Visual Acuity Study right eye 20/20, left eye 20/20, Pelvic exam uterus and ovaries are normal in size and location, valvula, cervix and vagina appears normal a:normal exam. no current issues. problem status: Chronic Obstructive Pulmonary Disease, being managed. administered immunization: FLUARIX p:Call office if any reaction from immunization. F/Up in one (1) year for annual check-up or sooner for new symptoms/problems as they arise.

s:pt presents with 4 weeks history of worsening critical shortness of breath, critical cough and critical dyspnea. she is a F aged 32 ys. pt reports that she smokes once or twice daily. drinks daily. o:Height 156 cm, Weight 43.4 kg, Temperature 37.1 C, Pulse 79, SystolicBP 104, DiastolicBP 63, Respiration 14, plum: accessory muscle use, Heart = RRR, Normal S1/S2, no murmurs, HEENT: WNL, rales Bil a:Chronic Obstructive Pulmonary Disease p:performed E/M Level 2 (established patient) - Completed, and referred patient to pulmonary disease.
s:a 32 yo f presents with 2 weeks history of worsening critical shortness of breath, critical cough and critical dyspnea. describes drinking an average of 12 drinks a week for about 4 years in her past. pt reports that she smokes once or twice daily. o:Height 157 cm, Weight 44.1 kg, Temperature 37.1 C, Pulse 80, SystolicBP 108, DiastolicBP 68, Respiration 15, plum: accessory muscle use, Heart = RRR, Normal S1/S2, no murmurs, HEENT: WNL, rales Bil a:Chronic Obstructive Pulmonary Disease p:performed E/M Level 3 (established patient) - Completed, and ordered Chest X-Ray.

s:a 31 YO F presents with 5 weeks history of Pyelonephritis. she does not smoke. she denies drinking alcohol. o:Height 65 in, Weight 154 lbs, Temperature 98.2 F, Pulse 72, SystolicBP 107, DiastolicBP 67, Respiration 15 a:Pyelonephritis p:performed E/M Level 2 (new patient) - Completed, and prescribed Ciprofloxacin - 500 mg 500 MG PO BID X 10 DAYS, and ordered Urinalysis.


s:57 yr old white m librarian presents today for wellness exam. he has a history of Chronic Renal Failure and Type 2 Diabetes. he has smoked 2 packs of cigarettes daily for 3 years. Patient reports that he never drinks alcohol. o:Height 69 in, Weight 115 lbs, Temperature 98.5 F, Pulse 80, SystolicBP 106, DiastolicBP 63, Respiration 14, Visual Acuity Study right eye 20/20, left eye 20/20, Testicular exam no lumps noted a:normal exam. Chronic Renal Failure. problem status: Type 2 Diabetes, being managed.  p:performed Visual Acuity Study, Testicular exam, and performed Periodic comprehensive preventive medicine..., new patient; 40-64 years - Completed, and prescribed Lisinopril - 20 mg daily, and ordered Basic Metabolic Panel, Urinalysis, Digital Rectal Exam, High-sensitivity fecal occult blood test, Flexible sigmoidoscopy, Lipid Profile, Intraoccular Pressure, Skin cancer screening.

"""


#def extract_phone_numbers(string):
    #r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')

    #return [re.sub(r'\D', '', number) for number in phone_numbers]


   


def extract_height(string):
    h=[]
    height = re.findall("Height.......", string)
    for item in height:
        for line in re.findall(r'\d+\s+\w{2}', item):
                h.append(line)
        dict1["height"] =h
        
    #print(len())
                
def extract_weight(string):
    w=[]
    weight = re.findall("Weight........",string)
    for item in weight:
        for line in re.findall('\d*\.?\d+\s\w{2}',item):
            w.append(line)
        dict1['weight'] = w
    #print(dict1)
                
def extract_temp(string):
    t=[]
    temp = re.findall("Temperature.......",string)
    for item in temp:
        for line in re.findall('\d*\.?\d+\s\w',item):
            t.append(line)
        dict1['temperature'] = t
    #print(dict1)
                
                
def extract_pulse(string):
    p=[]
    pulse = re.findall("Pulse...",string)
    for item in pulse:
        for line in re.findall('\d+',item):
            p.append(line)
        dict1['pulse'] = p
    #print(dict1)
                
                
def extract_systolicBP(string):
    s=[]
    bp1 = re.findall("SystolicBP....",string)
    for item in bp1:
        for line in re.findall('\d+',item):
            s.append(line)
        dict1['systolicBP'] = s
    #print(dict1)

def extract_diastolicBP(string):
    d=[]
    bp2 = re.findall("DiastolicBP....",string)
    for item in bp2:
        for line in re.findall('\d+',item):
            d.append(line)
        dict1['diastolicBP'] = d
    #print(dict1)           
              

def extract_respiration(string):
    r=[]
    resp = re.findall("Respiration...",string)
    
    for item in resp:
        for line in re.findall('\d+',item):
            r.append(line)
        dict1['respiration'] = r
    #print(dict1)
            
                
def extract_age(string):
    age9=[]
    age=re.findall(r'\s\d[1-9] \w*[y]+',string)
    age1=re.findall(r'\:\d[1-9] \w*[y,e,a,r,s,o,Y]',string)
    for i in age1:        
        p,ag=i.split(":" or ' ')
        age9.append(ag)
    
    #for item in (age+age9):
    dict1["age"] = age9+age
    #print(dict1)               

if __name__ == "__main__":
    dict1={ }
              
               

    
    H=extract_height(string)
    W=extract_weight(string)
    T=extract_temp(string)
    P=extract_pulse(string)
    SBP=extract_systolicBP(string)
    DBP=extract_diastolicBP(string)
    R=extract_respiration(string)
    A=extract_age(string)
    #print(dict1)
    data=dict1
    df=pd.DataFrame(data)
    print(df)
    #df

import platform

import pytest

import pyab3p
from hunflair_ab3p import HunFlairAb3P

texts = [
    "Respiratory syncytial viruses ( RSV ) are a subgroup of the paramyxoviruses.",
    "Bcl-2 is the best characterized inhibitor of apoptosis, although the molecular basis of this action is not fully understood. Using a protein interaction cloning procedure, we identified a human gene designated as bis (mapped to chromosome 10q25) that encoded a novel Bcl-2-interacting protein. Bis protein showed no significant homology with Bcl-2 family proteins and had no prominent functional motif. Co-immunoprecipitation analysis confirmed that Bis interacted with Bcl-2 in vivo. DNA transfection experiments indicated that Bis itself exerted only weak anti-apoptotic activity, but was synergistic with Bcl-2 in preventing Bax-induced and Fas-mediated apoptosis. These results suggest that Bis is a novel modulator of cellular anti-apoptotic activity that functions through its interaction with Bcl-2.",
    "Detection of abnormal cardiac adrenergic neuron activity in adriamycin-induced cardiomyopathy with iodine-125-metaiodobenzylguanidine.",
    "Treatment of psoriasis with azathioprine.",
    "Composition of Drosophila melanogaster proteome involved in fucosylated glycan metabolism.",
    "The locus for Friedreich ataxia (FRDA), a severe neurodegenerative disease, is tightly linked to markers D9S5 and D9S15, and analysis of rare recombination events has suggested the order cen-FRDA-D9S5-D9S15-qter. We report here the construction of a YAC contig extending 800 kb centromeric to D9S5 and the isolation of five new microsatellite markers from this region. In order to map these markers with respect to the FRDA locus, all within a 1-cM confidence interval, we sought to increase the genetic information of available FRDA families by considering homozygosity by descent and association with founder haplotypes in isolated populations. This approach allowed us to identify one phase-known recombination and one probable historic recombination on haplotypes from Reunion Island patients, both of which place three of the five markers proximal to FRDA. This represents the first identification of close FRDA flanking markers on the centromeric side. The two other markers allowed us to narrow the breakpoint of a previously identified distal recombination that is > 180 kb from D9S5 (26P). Taken together, the results place the FRDA locus in a 450-kb interval, which is small enough for direct search of candidate genes. A detailed rare cutter restriction map and a cosmid contig covering this interval were constructed and should facilitate the search of genes in this region..",
    "Sex differences in NMDA antagonist enhancement of morphine antihyperalgesia in a capsaicin model of persistent pain: comparisons to two models of acute pain.",
    "OBJECTIVE: To compare the antihypertensive efficacy of a new angiotensin II antagonist, valsartan, with a reference therapy, amlodipine. METHODS: One hundred sixty-eight adult outpatients with mild to moderate hypertension were randomly allocated in double-blind fashion and equal number to receive 80 mg valsartan or 5 mg amlodipine for 12 weeks. After 8 weeks of therapy, in patients whose blood pressure remained uncontrolled, 5 mg amlodipine was added to the initial therapy. Patients were assessed at 4, 8, and 12 weeks. The primary efficacy variable was change from baseline in mean sitting diastolic blood pressure at 8 weeks. Secondary variables included change in sitting systolic blood pressure and responder rates. RESULTS: Both valsartan and amlodipine were effective at lowering blood pressure at 4, 8, and 12 weeks. Similar decreases were observed in both groups, with no statistically significant differences between the groups for any variable analyzed. For the primary variable the difference was 0.5 mm Hg in favor of valsartan (p = 0.68; 95% confidence interval, -2.7 to 1.7). Responder rates at 8 weeks were 66.7% for valsartan and 60.2% for amlodipine (p = 0.39). Both treatments were well tolerated. The incidence of drug-related dependent edema was somewhat higher in the amlodipine group, particularly at a dose of 10 mg per day (2.4% for 80 mg valsartan; 3.6% for 5 mg amlodipine; 0% for valsartan plus 5 mg amlodipine; 14.3% for 10 mg amlodipine). CONCLUSIONS: The data show that valsartan is at least as effective as amlodipine in the treatment of mild to moderate hypertension. The results also show valsartan to be well tolerated and suggest that it is not associated with side effects characteristic of this comparator class, dihydropyridine calcium antagonists.",
    "Naloxone reversal of hypotension due to captopril overdose.",
    "The small nuclear ribonucleoprotein polypeptide N (SNRPN) gene is regarded as one of the candidates for Prader-Willi syndrome (PWS). We describe two sibs with typical PWS presenting deletion of SNRPN detected by fluorescence in situ hybridization (FISH). Neither a cytogenetically detectable 15q12 deletion nor a deletion for the D15S11, D15S10, and GABRB3 cosmid probes were found in either patient. This implies a smaller deletion limited to the PWS critical region. FISH with a SNRPN probe will permit analysis of PWS patients with limited deletions not detectable with other probes..",
    "Actinin-4, a novel actin-bundling protein associated with cell motility and cancer invasion.",
    "Low functional programming of renal AT2R mediates the developmental origin of glomerulosclerosis in adult offspring induced by prenatal caffeine exposure.",
    "Chromosomal translocations in human lipomas frequently create fusion transcripts encoding high mobility group (HMG) I-C DNA-binding domains and C-terminal sequences from different presumed transcription factors, suggesting a potential role for HMG I-C in the development of lipomas. To evaluate the role of the HMG I-C component, the three DNA-binding domains of HMG I-C have now been expressed in transgenic mice. Despite the ubiquitous expression of the truncated HMG I-C protein, the transgenic mice develop a selective abundance of fat tissue early in life, show marked adipose tissue inflammation, and have an abnormally high incidence of lipomas. These findings demonstrate that the DNA-binding domains of HMG I-C, in the absence of a C-terminal fusion partner, are sufficient to perturb adipogenesis and predispose to lipomas. We provide data supporting the central utility of this animal model as a tool to understand the molecular mechanisms underlying the development of one of the most common kind of human benign tumors..",
    "Proteinuria is a side effect of captopril treatment in hypertensive patients. The possibility of reproducing the same renal abnormality with captopril was examined in SHR. Oral administration of captopril at 100 mg/kg for 14 days failed to aggravate proteinuria pre-existing in SHR. Also, captopril treatment failed to potentiate or facilitate development of massive proteinuria invoked by puromycin aminonucleoside in SHR. Captopril had little or no demonstrable effects on serum electrolyte concentrations, excretion of urine, sodium and potassium, endogenous creatinine clearance, body weight, and food and water consumption. However, ketone bodies were consistently present in urine and several lethalities occurred during multiple dosing of captopril in SHR.",
    "A chronic schizophrenic patient was treated with an anticholinergic drug, trihexyphenidyl hydrochloride. The patient developed, paradoxically, sinus bradycardia. The reaction was specific to trihexyphenidyl and not to other anticholinergic drugs. This antidyskinetic drug is widely used in clinical psychiatric practice and physicians should be aware of this side effect.",
    "KRIT1 association with the integrin-binding protein ICAP-1: a new direction in the elucidation of cerebral cavernous malformations (CCM1) pathogenesis.",
    "Depression and sexual dysfunction have been related to side effects of topical beta-blockers. We performed a preliminary study in order to determine any difference between a non selective beta-blocker (timolol) and a selective beta-blocker (betaxolol) regarding CNS side effects. Eight glaucomatous patients chronically treated with timolol 0.5%/12h, suffering from depression diagnosed through DMS-III-R criteria, were included in the study. During the six-month follow up, depression was quantified through the Beck and Zung-Conde scales every two months. In a double blind cross-over study with control group, the patients under timolol treatment presented higher depression values measured through the Beck and the Zung-Conde scales (p < 0.001 vs control). These results suggest that betaxolol could be less of a depression-inducer than timolol in predisposed patients.",
    "The aim of the present study was to find out whether the metabotropic receptor 1 (mGluR1) and group II mGluRs, localized in the striatum, are involved in antiparkinsonian-like effects in rats. Haloperidol (1 mg/kg ip) induced parkinsonian-like muscle rigidity, measured as an increased resistance of a rat's hind foot to passive flexion and extension at the ankle joint. (RS)-1-aminoindan-1,5-dicarboxylic acid (AIDA; 0.5-15 microg/0.5 microl), a potent and selective mGluR1 antagonist, or (2R,4R)-4-aminopyrrolidine-2,4-dicarboxylate (2R,4R-APDC; 7.5-15 microg/0.5 microl), a selective group II agonist, was injected bilaterally into the striatum of haloperidol-treated animals. AIDA in doses of 7.5-15 microg/0.5 microl diminished the haloperidol-induced muscle rigidity. In contrast, 2R,4R-APDC injections were ineffective. The present results may suggest that the blockade of striatal mGluR1, but not the stimulation of group II mGluRs, may ameliorate parkinsonian muscle rigidity.",
    "The ETS family of proteins is a large group of transcription factors implicated in many aspects of normal hematopoietic development, as well as oncogenesis. For example, the TEL1/ETV6 (TEL1) gene is required for normal yolk sac angiogenesis, adult bone marrow hematopoiesis, and is rearranged or deleted in numerous leukemias. This report describes the cloning and characterization of a novel ETS gene that is highly related to TEL1 and is therefore called TEL2. The TEL2 gene consists of 8 exons spanning approximately 21 kilobases (kb) in human chromosome 6p21. Unlike the ubiquitously expressed TEL1 gene, however, TEL2 appears to be expressed predominantly in hematopoietic tissues. Antibodies raised against the C-terminus of the TEL2 protein were used to show that TEL2 localizes to the nucleus. All ETS proteins can bind DNA via the highly conserved ETS domain, which recognizes a purine-rich DNA sequence with a GGAA core motif. DNA binding assays show that TEL2 can bind the same consensus DNA binding sequence recognized by TEL1/ETV6. Additionally, the TEL2 protein is capable of associating with itself and with TEL1 in doubly transfected Hela cells, and this interaction is mediated through the pointed (PNT) domain of TEL1. The striking similarities of TEL2 to the oncogenic TEL1, its expression in hematopoietic tissues, and its ability to associate with TEL1 suggest that TEL2 may be an important hematopoietic regulatory protein.",
    "The nosology of the inborn errors of myelin metabolism has been stymied by the lack of molecular genetic analysis. Historically, Pelizaeus-Merzbacher disease has encompassed a host of neurologic disorders that present with a deficit of myelin, the membrane elaborated by glial cells that encircles and successively enwraps axons. We describe here a Pelizaeus-Merzbacher pedigree of the classical type, with X-linked inheritance, a typical clinical progression, and a pathologic loss of myelinating cells and myelin in the central nervous system. To discriminate variants of Pelizaeus-Merzbacher disease, a set of oligonucleotide primers was constructed to polymerase-chain-reaction (PCR) amplify and sequence the gene encoding proteolipid protein (PLP), a structural protein that comprises half of the protein of the myelin sheath. The PLP gene in one of two affected males and the carrier mother of this family exhibited a single base difference in the more than 2 kb of the PLP gene sequenced, a C----T transition that would create a serine substitution for proline at the carboxy end of the protein. Our results delineate the clinical features of Pelizaeus-Merzbacher disease, define the possible molecular pathology of this dysmyelinating disorder, and address the molecular classification of inborn errors of myelin metabolism. Patients with the classical form (type I) and the more severely affected, connatal variant of Pelizaeus-Merzbacher disease (type II) would be predicted to display mutation at the PLP locus. The other variants (types III-VI), which have sometimes been categorized as Pelizaeus-Merzbacher disease, may represent mutations in genes encoding other structural myelin proteins or proteins critical to myelination..",
    'Recently, the gene for the most common peroxisomal disorder, X-linked adrenoleukodystrophy (X-ALD), has been described encoding a peroxisomal membrane transporter protein. We analyzed the entire protein-coding sequence of this gene by reverse-transcription PCR, SSCP, and DNA sequencing in five patients with different clinical expression of X-ALD and in their female relatives; these clinical expressions were cerebral childhood ALD, adrenomyeloneuropathy (AMN), and " Addison disease only " (ADO) phenotype. In the three patients exhibiting the classical picture of severe childhood ALD we identified in the 5 portion of the X-ALD gene a 38-bp deletion that causes a frameshift mutation, a 3-bp deletion leading to a deletion of an amino acid in the ATP-binding domain of the ALD protein, and a missense mutation. In the patient with the clinical phenotype of AMN, a nonsense mutation in codon 212, along with a second site mutation at codon 178, was observed. Analysis of the patient with the ADO phenotype revealed a further missense mutation at a highly conserved position in the ALDP/PMP70 comparison. The disruptive nature of two mutations (i. e., the frameshift and the nonsense mutation) in patients with biochemically proved childhood ALD and AMN further strongly supports the hypothesis that alterations in this gene play a crucial role in the pathogenesis of X-ALD. Since the current biochemical techniques for X-ALD carrier detection in affected families lack sufficient reliability, our procedure described for systematic mutation scanning is also capable of improving genetic counseling and prenatal diagnosis',
]


@pytest.mark.parametrize("text", texts)
@pytest.mark.skipif(
    platform.system() != "Linux",
    reason="HunFlairAb3P only works on linux, hence we cannot test it on windows",
)
def test_regression(text: str) -> None:
    hunflair_ab3p = HunFlairAb3P()
    ab3p = pyab3p.Ab3p()

    hunflair_res = hunflair_ab3p.get_abbreviations(text)
    ab3p_res = list(set([(r.short_form, r.long_form) for r in ab3p.get_abbrs(text)]))

    assert ab3p_res == hunflair_res


@pytest.mark.skipif(
    platform.system() != "Linux",
    reason="HunFlairAb3P only works on linux, hence we cannot test it on windows",
)
def test_large_regression(testdata) -> None:
    texts = testdata("texts.txt").read_text(encoding="utf-8").split("\n")

    hunflair_ab3p = HunFlairAb3P()
    ab3p = pyab3p.Ab3p()

    for text in texts:
        hunflair_res = hunflair_ab3p.get_abbreviations(text)
        ab3p_res = list(
            {r.short_form: r.long_form for r in ab3p.get_abbrs(text)}.items()
        )

        assert ab3p_res == hunflair_res


def test_snapshot(test_snapshots, testdata) -> None:
    ab3p = pyab3p.Ab3p()

    result = []
    for text in texts:
        rows = []
        for r in ab3p.get_abbrs(text):
            rows.append(
                {
                    "sf": r.short_form,
                    "lf": r.long_form,
                    "prec": r.prec,
                    "strat": r.strat,
                }
            )
        result.append(rows)

    test_snapshots(result, testdata("bio-output.json"))


def test_large_snapshot(test_snapshots, testdata) -> None:
    ab3p = pyab3p.Ab3p()

    texts = testdata("texts.txt").read_text(encoding="utf-8").split("\n")

    result = []

    for text in texts:
        rows = []
        for r in ab3p.get_abbrs(text):
            rows.append(
                {
                    "sf": r.short_form,
                    "lf": r.long_form,
                    "prec": r.prec,
                    "strat": r.strat,
                }
            )
        result.append(rows)

    test_snapshots(result, testdata("bio-large-output.json"))

import taxcalc

SHOW_RUNTIME = False  # Flag to display RuntimeWarnings when run model

REFORM_DIR = "OUTPUT_REFORM"
BASELINE_DIR = "OUTPUT_BASELINE"

# Default year for model runs
DEFAULT_START_YEAR = 2022


VAR_LABELS = {
    "Y": "GDP ($Y_t$)",
    "C": "Consumption ($C_t$)",
    "L": "Labor ($L_t$)",
    "G": "Government Expenditures ($G_t$)",
    "TR": "Lump sum transfers ($TR_t$)",
    "B": "Wealth ($B_t$)",
    "I_total": "Investment ($I_t$)",
    "K": "Capital Stock ($K_t$)",
    "K_d": "Domestically-owned Capital Stock ($K^d_t$)",
    "K_f": "Foreign-owned Capital Stock ($K^f_t$)",
    "D": "Government Debt ($D_t$)",
    "D_d": "Domestically-owned Gov Debt ($D^d_t$)",
    "D_f": "Foreign-owned Gov Debt ($D^f_t$)",
    "r": "Real interest rate ($r_t$)",
    "r_gov": "Real interest rate on gov debt ($r_{gov,t}$)",
    "r_hh": "Real interest rate on HH portfolio ($r_{hh,t}$)",
    "w": "Wage rate",
    "BQ": "Aggregate bequests ($BQ_{j,t}$)",
    "total_tax_revenue": "Total tax revenue ($REV_t$)",
    "business_tax_revenue": "Business tax revenue",
    "iit_revenue": "Individual income tax revenue",
    "payroll_tax_revenue": "Payroll tax revenue",
    "iit_payroll_tax_revenue": "IIT and payroll tax revenue",
    "n_mat": "Labor Supply ($n_{j,s,t}$)",
    "c_path": "Consumption ($c_{j,s,t}$)",
    "bmat_splus1": "Savings ($b_{j,s+1,t+1}$)",
    "bq_path": "Bequests ($bq_{j,s,t}$)",
    "bmat_s": "Savings ($b_{j,s,t}$)",
    "y_before_tax_mat": "Before tax income",
    "etr_path": "Effective Tax Rate ($ETR_{j,s,t}$)",
    "mtrx_path": "Marginal Tax Rate, Labor Income ($MTRx_{j,s,t}$)",
    "mtry_path": "Marginal Tax Rate, Capital Income ($MTRy_{j,s,t}$)",
    "tax_path": "Total Taxes",
    "nssmat": "Labor Supply ($\\bar{n}_{j,s}$)",
    "bssmat_s": "Savings ($\\bar{b}_{j,s}$)",
    "bssmat_splus1": "Savings ($\\bar{b}_{j,s+1}$)",
    "cssmat": "Consumption ($\\bar{c}_{j,s}$)",
    "yss_before_tax_mat": "Before-tax Income",
    "etr_ss": "Effective Tax Rate ($\\bar{ETR}_{j,s}$)",
    "mtrx_ss": "Marginal Tax Rate, Labor Income ($\\bar{MTRx}_{j,s}$)",
    "mtry_ss": "Marginal Tax Rate, Capital Income ($\\bar{MTRy}_{j,s}$)",
    "ETR": "Effective Tax Rates",
    "MTRx": "Marginal Tax Rates on Labor Income",
    "MTRy": "Marginal Tax Rates on Capital Income",
    "etr": "Effective Tax Rates",
    "mtrx": "Marginal Tax Rates on Labor Income",
    "mtry": "Marginal Tax Rates on Capital Income",
    "Yss": "GDP ($\\bar{Y}$)",
    "Css": "Consumption ($\\bar{C}$)",
    "Lss": "Labor ($\\bar{L}$)",
    "Gss": "Government Expenditures ($\\bar{G}$)",
    "TR_ss": "Lump sum transfers, ($\\bar{TR}$)",
    "Bss": "Wealth ($\\bar{B}$)",
    "Iss_total": "Investment ($\\bar{I}$)",
    "Kss": "Capital Stock ($\\bar{K}$)",
    "K_d_ss": "Domestically-owned Capital Stock ($\\bar{K}^d$)",
    "K_f_ss": "Foreign-owned Capital Stock ($\\bar{K}^f$)",
    "Dss": "Government Debt ($\\bar{D}$)",
    "D_d_ss": "Domestically-owned Gov Debt ($\\bar{D}^d$)",
    "D_f_ss": "Foreign-owned Gov Debt ($\\bar{D}^f$)",
    "rss": "Real interest rate ($\\bar{r}$)",
    "r_gov_ss": "Real interest rate on gov debt ($\\bar{r}_{gov}$)",
    "r_hh_ss": "Real interest rate on HH portfolio ($\\bar{r}_{hh}$)",
    "wss": "Wage rate ($\\bar{w}$)",
    "BQss": "Aggregate bequests ($\\bar{BQ}_{j}$)",
    "debt_service_ss": "Debt service cost ($\\bar{r}_{gov}\\bar{D}$)",
    "D/Y": "Debt to GDP ratio",
    "T_Pss": "Government Pensions",
}

ToGDP_LABELS = {
    "D": "Debt-to-GDP ($D_{t}/Y_t$)",
    "D_d": "Domestically-owned Debt-to-GDP ($D^d_{t}/Y_t$)",
    "D_f": "Foreign-owned Debt-to-GDP ($D^f_{t}/Y_t$)",
    "G": "Govt Spending-to-GDP ($G_{t}/Y_t$)",
    "K": "Capital-Output Ratio ($K_{t}/Y_t$)",
    "K_d": "Domestically-owned Capital-Output Ratio ($K^d_{t}/Y_t$)",
    "K_f": "Foreign-owned Capital-Output Ratio ($K^f_{t}/Y_t$)",
    "C": "Consumption-Output Ratio ($C_{t}/Y_t$)",
    "I": "Investment-Output Ratio ($I_{t}/Y_t$)",
    "total_tax_revenue": "Tax Revenue-to-GDP ($REV_{t}/Y_t$)",
}

GROUP_LABELS = {
    7: {
        0: "0-25%",
        1: "25-50%",
        2: "50-70%",
        3: "70-80%",
        4: "80-90%",
        5: "90-99%",
        6: "Top 1%",
    },
    9: {
        0: "0-25%",
        1: "25-50%",
        2: "50-70%",
        3: "70-80%",
        4: "80-90%",
        5: "90-99%",
        6: "99-99.5%",
        7: "99.5-99.9%",
        8: "Top 0.1%",
    },
    10: {
        0: "0-25%",
        1: "25-50%",
        2: "50-70%",
        3: "70-80%",
        4: "80-90%",
        5: "90-99%",
        6: "99-99.5%",
        7: "99.5-99.9%",
        8: "99.9-99.99%",
        9: "Top 0.01%",
    },
}

CBO_UNITS = {
    "Y": r"Billions of ₹",
    "r": "Percent",
    "w_growth": "Percent",
    "L_growth": "Percent",
    "I_total": r"Billions of ₹",
    "L": "2012=100",
    "C": r"Billions of ₹",
    "agg_pension_outlays": r"Billions of ₹",
    "G": r"Billions of ₹",
    "iit_revenue": r"Billions of ₹",
    "payroll_tax_revenue": r"Billions of ₹",
    "business_tax_revenue": r"Billions of ₹",
    "wL": r"Billions of ₹",
    "D": r"Billions of ₹",
}

PARAM_LABELS = {
    "start_year": ["Initial year", r"$\texttt{start_year}$"],
    # 'Gamma': ['Initial distribution of savings', r'\hat{\Gamma}_{0}'],
    # 'N': ['Initial population', 'N_{0}'],
    "omega": ["Population by age over time", r"${{\omega_{s,t}}}_{s=1}^{S}$"],
    # 'fert_rates': ['Fertility rates by age',
    #                r'\left{f_{s}\right}_{s=1}^{S}'],
    "imm_rates": ["Immigration rates by age", r"${{i_{s}}}_{s=1}^{S}$"],
    "rho": ["Mortality rates by age", r"${{\rho_{s}}}_{s=1}^{S}$"],
    "e": ["Deterministic ability process", r"${{e_{j,s}}}_{j,s=1}^{J,S}$"],
    "lambdas": [
        "Lifetime income group percentages",
        r"${{\lambda_{j}}}_{j=1}^{J}$",
    ],
    "J": ["Number of lifetime income groups", "$J$"],
    "S": ["Maximum periods in economically active individual life", "$S$"],
    "E": ["Number of periods of youth economically outside the model", "$E$"],
    "T": ["Number of periods to steady-state", "$T$"],
    "retirement_age": ["Retirement age", "$R$"],
    "ltilde": ["Maximum hours of labor supply", r"$\tilde{l}$"],
    "beta": ["Discount factor", r"$\beta$"],
    "sigma": ["Coefficient of constant relative risk aversion", r"$\sigma$"],
    "frisch": ["Frisch elasticity of labor supply", r"$\nu$"],
    "b_ellipse": ["Scale parameter in utility of leisure", "$b$"],
    "upsilon": ["Shape parameter in utility of leisure", r"$\upsilon$"],
    # 'k': ['Constant parameter in utility of leisure', 'k'],
    "chi_n": [
        "Disutility of labor level parameters",
        r"$\left{\chi^{n}_{s}\right}_{s=1}^{S}$",
    ],
    "chi_b": [
        "Utility of bequests level parameters",
        r"$\left{\chi^{b}_{j}\right}_{j=1}^{J}$",
    ],
    "use_zeta": [
        "Whether to distribute bequests between lifetime income groups",
        r"$\texttt{use_zeta}$",
    ],
    "zeta": ["Distribution of bequests", r"$\zeta$"],
    "Z": ["Total factor productivity", "$Z_{t}$"],
    "gamma": ["Capital share of income", r"$\gamma$"],
    "epsilon": [
        "Elasticity of substitution between capital and labor",
        r"\varepsilon",
    ],
    "delta": ["Capital depreciation rate", r"$\delta$"],
    "g_y": [
        "Growth rate of labor augmenting technological progress",
        r"$g_{y}$",
    ],
    "tax_func_type": [
        "Functional form used for income tax functions",
        r"$\texttt{tax_func_type}$",
    ],
    "analytical_mtrs": [
        "Whether use analytical MTRs or estimate MTRs",
        r"$\texttt{analytical_mtrs}$",
    ],
    "age_specific": [
        "Whether use age-specific tax functions",
        r"$\texttt{age_specific}$",
    ],
    "tau_payroll": ["Payroll tax rate", r"$\tau^{p}_{t}$"],
    # 'theta': ['Replacement rate by average income',
    #           r'\left{\theta_{j}\right}_{j=1}^{J}'],
    "tau_bq": ["Bequest (estate) tax rate", r"$\tau^{BQ}_{t}}$"],
    "tau_b": ["Entity-level business income tax rate", r"$\tau^{b}_{t}$"],
    "delta_tau": [
        "Rate of depreciation for tax purposes",
        r"$\delta^{\tau}_{t}$",
    ],
    "tau_c": ["Consumption tax rates", r"$\tau^{c}_{t,s,j}$"],
    "h_wealth": ["Coefficient on linear term in wealth tax function", "$H$"],
    "m_wealth": ["Constant in wealth tax function", "$M$"],
    "p_wealth": ["Coefficient on level term in wealth tax function", "$P$"],
    "budget_balance": [
        "Whether have a balanced budget in each period",
        r"$\texttt{budget_balance}$",
    ],
    "baseline_spending": [
        "Whether level of spending constant between "
        + "the baseline and reform runs",
        r"$\texttt{baseline_spending}$",
    ],
    "alpha_T": ["Transfers as a share of GDP", r"$\alpha^{T}_{t}$"],
    "eta": ["Distribution of transfers", r"$\eta_{j,s,t}$"],
    "alpha_G": ["Government spending as a share of GDP", r"$\alpha^{G}_{t}$"],
    "tG1": ["Model period in which budget closure rule starts", r"$t_{G1}$"],
    "tG2": ["Model period in which budget closure rule ends", r"$t_{G2}$"],
    "rho_G": ["Budget closure rule smoothing parameter", r"$\rho_{G}$"],
    "debt_ratio_ss": ["Steady-state Debt-to-GDP ratio", r"$\bar{\alpha}_{D}$"],
    "initial_debt_ratio": [
        "Initial period Debt-to-GDP ratio",
        r"$\alpha_{D,0}$",
    ],
    "r_gov_scale": [
        "Scale parameter in government interest rate wedge",
        r"$\tau_{d,t}$",
    ],
    "r_gov_shift": [
        "Shift parameter in government interest rate wedge",
        r"$\mu_{d,t}$",
    ],
    "AIME_num_years": [
        "Number of years over which compute AIME",
        r"$\texttt{AIME_num_years}$",
    ],
    "AIME_bkt_1": ["First AIME bracket threshold", r"$\texttt{AIME_bkt_1}$"],
    "AIME_bkt_2": ["Second AIME bracket threshold", r"$\texttt{AIME_bkt_2}$"],
    "PIA_rate_bkt_1": [
        "First AIME bracket PIA rate",
        r"$\texttt{PIA_rate_bkt_1}$",
    ],
    "PIA_rate_bkt_2": [
        "Second AIME bracket PIA rate",
        r"\texttt{PIA_rate_bkt_2}",
    ],
    "PIA_rate_bkt_3": [
        "Third AIME bracket PIA rate",
        r"$\texttt{PIA_rate_bkt_3}$",
    ],
    "PIA_maxpayment": ["Maximum PIA payment", r"$\texttt{PIA_maxpayment}$"],
    "PIA_minpayment": ["Minimum PIA payment", r"$\texttt{PIA_maxpayment}$"],
    "replacement_rate_adjust": [
        "Adjustment to replacement rate",
        r"$theta_{adj,t}$",
    ],
    "world_int_rate": ["World interest rate", r"$r^{*}_{t}$"],
    "initial_foreign_debt_ratio": [
        "Share of government debt held by foreigners in initial period",
        r"$D_{f,0}$",
    ],
    "zeta_D": [
        "Share of new debt issues purchased by foreigners",
        r"$\zeta_{D, t}$",
    ],
    "zeta_K": [
        "Share of excess capital demand satisfied by foreigners",
        r"$\zeta_{K, t}$",
    ],
    "nu": ["Dampening parameter for TPI", r"$\xi$"],
    "maxiter": ["Maximum number of iterations for TPI", r"$\texttt{maxiter}$"],
    "mindist_SS": ["SS solution tolerance", r"$\texttt{mindist_SS}$"],
    "mindist_TPI": ["TPI solution tolerance", r"$\texttt{mindist_TPI}$"],
}

# Ignoring the following:
# 'starting_age', 'ending_age', 'constant_demographics',
# 'constant_rates', 'zero_taxes'


"""
Create dictionaries to map micro categories to broad groups
"""
cons_dict = {
    "Food": [
        "cagri",
        "clani",
        "cfore",
        "cfish",
        "cwatr",
        "cmeat",
        "cpfis",
        "cvege",
        "cfrui",
        "cfats",
        "cdair",
        "cgrai",
        "cstar",
        "cafee",
        "cbake",
        "csuga",
        "cconf",
        "cpast",
        "cofoo",
        "calcb",
        "csftd",
        "ctoba",
    ],
    "Energy and extraction": [
        "ccoal",
        "cmore",
        "comin",
        "celcg",
    ],
    "Non-durables": [
        "ctexf",
        "ctexm",
        "ccarp",
        "cotex",
        "cknit",
        "cwear",
        "cleat",
        "cfoot",
        "cwood",
        "cpapp",
        "cprnt",
        "cpetr",
        "cbchm",
        "cfert",
        "cpain",
        "cphar",
        "csoap",
        "coche",
        "ctyre",
        "corub",
        "cplas",
        "cglas",
        "ccera",
        "cclay",
        "ccmnt",
        "cconc",
        "conmp",
        "cfurn",
        "cjewl",
        "comnf",
        "cwast",
    ],
    "Durables": [
        "cirst",
        "cnfme",
        "cstrm",
        "ctank",
        "cofbm",
        "cengt",
        "cpump",
        "cgear",
        "clift",
        "cgenm",
        "cspcm",
        "cdoma",
        "coffm",
        "celcm",
        "crdtv",
        "cmeda",
        "cmtvp",
        "cship",
        "crail",
        "cairc",
        "coteq",
        "ccnst",
    ],
    "Services": [
        "ccsrv",
        "ctrad",
        "cacco",
        "ccats",
        "cptrp",
        "cftrp",
        "ctrps",
        "cpost",
        "celcd",
        "cwatd",
        "cfins",
        "cinsp",
        "cofin",
        "creal",
        "crent",
        "crsea",
        "clacc",
        "cobus",
        "ctelc",
        "csupp",
        "cmnfs",
        "cpuba",
        "ceduc",
        "cheal",
        "cosrv",
    ],
}
prod_dict = {
    "Primary": [
        "aagri",
        "afore",
        "afish",
        "acoal",
        "agold",
        "amore",
        "aomin",
    ],
    "Energy": [
        "aelcg",
    ],
    "Tertiary": [
        "awtrd",
        "artrd",
        "amtvs",
        "aacct",
        "altrp",
        "awtrp",
        "aatrp",
        "atrps",
        "apost",
        "afins",
        "ainsp",
        "aofin",
        "areal",
        "arent",
        "acomp",
        "arsea",
        "aobus",
        "apuba",
        "aeduc",
        "aheal",
        "awast",
        "amorg",
        "arecr",
        "aoact",
        "anobs",
    ],
    "Secondary Ex Energy": [
        "afood",
        "abevt",
        "aweav",
        "aknit",
        "aleat",
        "afoot",
        "awood",
        "apapr",
        "aprnt",
        "apetr",
        "abchm",
        "aochm",
        "arubb",
        "aplas",
        "aglss",
        "anmmi",
        "abisc",
        "anfme",
        "afabm",
        "amach",
        "aemch",
        "ardtv",
        "amopt",
        "amtvp",
        "aotrp",
        "afurn",
        "aomnf",
        "awatd",
        "acnst",
    ],
}

"""
Read in SAM file
"""
# Read in SAM file
storage_options = {"User-Agent": "Mozilla/5.0"}
SAM_path = "https://www.wider.unu.edu/sites/default/files/Data/SASAM-2015-Data-Resource.xlsx"
SAM = pd.read_excel(
    SAM_path,
    sheet_name="Micro SAM 2015",
    skiprows=6,
    index_col=0,
    storage_options=storage_options,
)


def get_alpha_c(SAM, cons_dict):
    """
    Calibrate the alpha_c vector, showing the shares of household
    expenditures for each consumption category

    Args:
        SAM (pd.DataFrame): SAM file
        cons_dict (dict): Dictionary of consumption categories

    Returns:
        alpha_c (dict): Dictionary of shares of household expenditures
    """
    overall_sum = 0
    for key, value in cons_dict.items():
        # note the subtraction of the row to focus on domestic consumption
        categroy_total = (
            SAM.loc[SAM.index.isin(value), "total"].sum()
            - SAM.loc[SAM.index.isin(value), "row"].sum()
        )
        alpha_c[key] = categroy_total
        overall_sum += categroy_total
    for key, value in cons_dict.items():
        alpha_c[key] = alpha_c[key] / overall_sum

    return alpha_c


def get_io_matrix(SAM, cons_dict, prod_dict):
    """
    Calibrate the io_matrix array.  This array relates the share of each
    production category in each consumption category

    Args:
        SAM (pd.DataFrame): SAM file
        cons_dict (dict): Dictionary of consumption categories
        prod_dict (dict): Dictionary of production categories

    Returns:
        io_df (pd.DataFrame): Dataframe of io_matrix
    """
    # Create initial matrix as dataframe of 0's to fill in
    io_dict = {}
    for key in prod_dict.keys():
        io_dict[key] = np.zeros(len(cons_dict.keys()))
    io_df = pd.DataFrame(io_dict, index=cons_dict.keys())
    # Fill in the matrix
    # Note, each cell in the SAM represents a payment from the columns
    # account to the row account
    # (see https://www.un.org/en/development/desa/policy/capacity/presentations/manila/6_sam_mams_philippines.pdf)
    # We are thus going to take the consumption categories from rows and
    # the production categories from columns
    for ck, cv in cons_dict.items():
        for pk, pv in prod_dict.items():
            io_df.loc[io_df.index == ck, pk] = SAM.loc[
                SAM.index.isin(cv), pv
            ].values.sum()
    # change from levesl to share (where each row sums to one)
    io_df = io_df.div(io_df.sum(axis=1), axis=0)

    return io_df


import pandas as pd


"""
Create dictionaries to map micro categories to broad groups
Codes come from https://www.wider.unu.edu/database/2015-social-accounting-matrix-south-africa
"""
CONS_DICT = {
    "Food": [
        "cagri",
        "clani",
        "cfore",
        "cfish",
        "cwatr",
        "cmeat",
        "cpfis",
        "cvege",
        "cfrui",
        "cfats",
        "cdair",
        "cgrai",
        "cstar",
        "cafee",
        "cbake",
        "csuga",
        "cconf",
        "cpast",
        "cofoo",
        "calcb",
        "csftd",
        "ctoba",
    ],
    "Energy and extraction": [
        "ccoal",
        "cmore",
        "comin",
        "celcg",
    ],
    "Non-durables": [
        "ctexf",
        "ctexm",
        "ccarp",
        "cotex",
        "cknit",
        "cwear",
        "cleat",
        "cfoot",
        "cwood",
        "cpapp",
        "cprnt",
        "cpetr",
        "cbchm",
        "cfert",
        "cpain",
        "cphar",
        "csoap",
        "coche",
        "ctyre",
        "corub",
        "cplas",
        "cglas",
        "ccera",
        "cclay",
        "ccmnt",
        "cconc",
        "conmp",
        "cfurn",
        "cjewl",
        "comnf",
        "cwast",
    ],
    "Durables": [
        "cirst",
        "cnfme",
        "cstrm",
        "ctank",
        "cofbm",
        "cengt",
        "cpump",
        "cgear",
        "clift",
        "cgenm",
        "cspcm",
        "cdoma",
        "coffm",
        "celcm",
        "crdtv",
        "cmeda",
        "cmtvp",
        "cship",
        "crail",
        "cairc",
        "coteq",
        "ccnst",
    ],
    "Services": [
        "ccsrv",
        "ctrad",
        "cacco",
        "ccats",
        "cptrp",
        "cftrp",
        "ctrps",
        "cpost",
        "celcd",
        "cwatd",
        "cfins",
        "cinsp",
        "cofin",
        "creal",
        "crent",
        "crsea",
        "clacc",
        "cobus",
        "ctelc",
        "csupp",
        "cmnfs",
        "cpuba",
        "ceduc",
        "cheal",
        "cosrv",
    ],
}
PROD_DICT = {
    "Primary": [
        "aagri",
        "afore",
        "afish",
        "acoal",
        "agold",
        "amore",
        "aomin",
    ],
    "Energy": [
        "aelcg",
    ],
    "Tertiary": [
        "awtrd",
        "artrd",
        "amtvs",
        "aacct",
        "altrp",
        "awtrp",
        "aatrp",
        "atrps",
        "apost",
        "afins",
        "ainsp",
        "aofin",
        "areal",
        "arent",
        "acomp",
        "arsea",
        "aobus",
        "apuba",
        "aeduc",
        "aheal",
        "awast",
        "amorg",
        "arecr",
        "aoact",
        "anobs",
    ],
    "Secondary Ex Energy": [
        "afood",
        "abevt",
        "aweav",
        "aknit",
        "aleat",
        "afoot",
        "awood",
        "apapr",
        "aprnt",
        "apetr",
        "abchm",
        "aochm",
        "arubb",
        "aplas",
        "aglss",
        "anmmi",
        "abisc",
        "anfme",
        "afabm",
        "amach",
        "aemch",
        "ardtv",
        "amopt",
        "amtvp",
        "aotrp",
        "afurn",
        "aomnf",
        "awatd",
        "acnst",
    ],
}

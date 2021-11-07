import numpy as np
import pandas as pd
import fdb
import os

pd.options.mode.chained_assignment = None

filepath=os.path.abspath("C:\\Users\\niik\\IdeaProjects\\learn\\.idea\\ndv\\mps_ndv.xlsm")
class_d = 3
calc_id_tbl5 = 134
calc_id_tbl5cc = 134

#pathout
filepath_wo_ext=os.path.splitext(filepath)[0]
filefolder=os.path.dirname(filepath_wo_ext)
filename=os.path.basename(filepath_wo_ext)
filepathout=os.path.abspath(filefolder+'\\'+filename+'_calc.xlsx')

# guide
df_guide = pd.read_excel(filepath,sheet_name='quide',na_values='')
#print(df_guide[['code','PDKmr']])

df_guide_pdkmr = df_guide[['substance_code','name_quide','class_op','PDKmr']][df_guide['PDKmr']!=0]
df_guide_pdkmr['pdk'] = 'ПДКмр'
df_guide_pdkmr = df_guide_pdkmr.rename(columns={"PDKmr":"pdk_values"})
#print(df_guide_pdkmr)

df_guide_pdkss = df_guide[['substance_code','name_quide','class_op','PDKss']][df_guide['PDKss']!=0]
df_guide_pdkss['pdk'] = 'ПДКсс'
df_guide_pdkss = df_guide_pdkss.rename(columns={'PDKss':'pdk_values'})
#print(df_guide_pdkss)

df_guide_pdksg = df_guide[['substance_code','name_quide','class_op','PDKsg']][df_guide['PDKsg']!=0]
df_guide_pdksg['pdk'] = 'ПДКсг'
df_guide_pdksg = df_guide_pdksg.rename(columns={'PDKsg':'pdk_values'})
#print(df_guide_pdksg)

df_guide_obuv = df_guide[['substance_code','name_quide','class_op','OBUV']][df_guide['OBUV']!=0]
df_guide_obuv['pdk'] = 'ОБУВ'
df_guide_obuv = df_guide_obuv.rename(columns={'OBUV':'pdk_values'})
#print(df_guide_obuv)

df_guide_pdk = pd.concat([df_guide_pdkmr[['substance_code','name_quide','class_op','pdk','pdk_values']],df_guide_pdkss[['substance_code','name_quide','class_op','pdk','pdk_values']],df_guide_pdksg[['substance_code','name_quide','class_op','pdk','pdk_values']],df_guide_obuv[['substance_code','name_quide','class_op','pdk','pdk_values']]],join='outer')

#print(df_guide_pdk)

# ishod
df_ishod_source = pd.read_excel(filepath,sheet_name='ishod_source',na_values='')
#print(df_ishod_source)

df_ishod_substance = pd.read_excel(filepath,sheet_name='ishod_subst',na_values='')
#print(df_ishod_substance)

df_ishod_all = pd.merge(df_ishod_substance,df_ishod_source,how='inner',on='source')
#print(df_ishod_all)

# ishod + guide
df_ishod_guide = pd.merge(df_ishod_all,df_guide,how='left',on='substance_code')
#print(df_ishod_guide)

df_ishod_guide.loc[df_ishod_guide['ob_r_source'] != 0,'g_norm'] = df_ishod_guide['g_s_subst'] * 1000 / df_ishod_guide['ob_r_source']
df_ishod_guide.loc[df_ishod_guide['ob_r_source'] == 0,'g_norm'] = 0

df_subs_unique=df_ishod_guide.drop_duplicates(subset=['substance_code'])
#print(df_subs_unique)

# norm/nenorm
if class_d == 3:
    df_ishod_guide_2 = df_ishod_guide[(df_ishod_guide['class_op']==1) | (df_ishod_guide['class_op'] == 2)]
    df_ishod_guide_2_nenorm = df_ishod_guide[(df_ishod_guide['class_op']!=1) & (df_ishod_guide['class_op'] != 2)]
if class_d == 2:
    df_ishod_guide_2 = df_ishod_guide[(df_ishod_guide['class_op']==1)]
    df_ishod_guide_2_nenorm = df_ishod_guide[(df_ishod_guide['class_op']!=1)]

df_ishod_guide_norm = df_ishod_guide_2.pivot_table(index=['substance_code','name_quide','class_op','code_pp','name_pp'],values='t_year_subst',aggfunc=np.sum)
df_ishod_guide_nenorm = df_ishod_guide_2_nenorm.pivot_table(index=['substance_code','name_quide','class_op','code_pp','name_pp'],values='t_year_subst',aggfunc=np.sum,fill_value=0)

#tbl 4
df_guide_pdk = df_guide_pdk.merge(df_ishod_guide_norm,how='inner',on='substance_code')
df_guide_tbl4 = df_guide_pdk.groupby(['substance_code','name_quide','class_op','t_year_subst','pdk']).sum()

#tbl 6
df_guide_tbl6 = df_ishod_guide_2[['substance_code','division_source','source','g_s_subst','t_year_subst','name_quide']]#.sort_values(by=['substance_code','source'],ascending=True)
df_guide_tbl6['pdv']='ПДВ'

df_guide_tbl6_subtotals = df_guide_tbl6.pivot_table(index=['substance_code'],values=['g_s_subst','t_year_subst'],aggfunc=np.sum)

df_guide_tbl6_names = df_guide_tbl6.pivot_table(index=['substance_code'],values=['name_quide'],aggfunc=np.max)

df_guide_tbl7 = df_guide_tbl6_subtotals.join(df_guide_tbl6_names,how='inner')

df_guide_tbl6_subtotals['division_source'] = 'всего по ЗВ:'
df_guide_tbl6_subtotals['pdv']=''
df_guide_tbl6_subtotals['source']=9999
df_guide_tbl6_subtotals['substance_code'] = df_guide_tbl6_subtotals.index

df_guide_tbl6_names['division_source']= df_guide_tbl6_names.index
df_guide_tbl6_names=df_guide_tbl6_names.astype({'division_source':str,'name_quide': str})
df_guide_tbl6_names['division_source']= 'Наименование загрязняющего вещества: ' + df_guide_tbl6_names['division_source'] + '/' + df_guide_tbl6_names['name_quide']
df_guide_tbl6_names['pdv']=''
df_guide_tbl6_names['source']=-9999
df_guide_tbl6_names['substance_code'] = df_guide_tbl6_names.index
df_guide_tbl6_names['g_s_subst']=''
df_guide_tbl6_names['t_year_subst']=''

df_guide_tbl6_all = pd.concat([df_guide_tbl6[['substance_code','division_source','source','g_s_subst','t_year_subst','pdv']],\
                               df_guide_tbl6_subtotals[['substance_code','division_source','source','g_s_subst','t_year_subst','pdv']],\
                               df_guide_tbl6_names[['substance_code','division_source','source','g_s_subst','t_year_subst','pdv']]],join='outer').sort_values(by=['substance_code','source'],ascending=True)

df_guide_tbl6_all.loc[df_guide_tbl6_all['source'] == 9999,'source'] = ''
df_guide_tbl6_all.loc[df_guide_tbl6_all['source'] == -9999,'source'] = ''

# tbl7
df_guide.set_index('substance_code', inplace=True, drop=True)
df_guide_tbl7= df_guide_tbl7.merge(df_guide,how='inner')
df_guide_tbl7['pdv']='ПДВ'

#print(df_guide_tbl7.index)
#print(df_guide)

# tbl 5
#con = fdb.connect(dsn='//127.0.0.1:D:\integral_bd\integral_bd\EXAMPLE_4.ECODB', user='SYSDBA', password='masterkey')
con = fdb.connect(host='127.0.0.1', database='D:\integral_bd\integral_bd\EXAMPLE_4.ECODB', user='sysdba', password='masterkey', charset='UTF8')
cur = con.cursor()
query = "WITH res as (\
    SELECT RESCODE.CODE AS subcode, SUBST.NAME AS subname, RASPOINT.CODE AS pointname, RESDATA.N_FON, RESDATA.N_C, RASPOINT.NZ_TYPE, IST.IST_NN, SRES.PRC, CECH.NAME AS cechname\
    FROM RESDATA\
    JOIN RESTYPE ON RESTYPE.ID = RESDATA.RESTYPE_ID\
    JOIN RASPOINT ON RASPOINT.ID = RESDATA.RASPOINT_ID\
    JOIN RESCODE ON RESCODE.ID = RESTYPE.RESCODE_ID\
    JOIN RESSHARE ON RESSHARE.RESDATA_ID = RESDATA.ID\
    JOIN SRES ON SRES.RESSHARE_ID = RESSHARE.ID\
    JOIN IST ON IST.ID = SRES.IST_ID\
    JOIN CECH ON CECH.ID = IST.CH_ID\
    JOIN SUBST ON SUBST.CODE = RESCODE.CODE\
    WHERE RESCODE.CVRUN_ID = " + str(calc_id_tbl5) + "\
    ),\
    res2 as(\
    SELECT subcode, NZ_TYPE, MAX(N_C) AS N_C_MAX\
    FROM res\
    GROUP BY subcode, NZ_TYPE\
    ),\
    res3 as(\
    SELECT res2.subcode, 	res2.NZ_TYPE, res2.N_C_MAX, max(res.PRC) AS PRC_MAX\
    FROM res\
    INNER JOIN res2\
    ON res2.subcode = res.subcode AND res2.NZ_TYPE = res.NZ_TYPE AND res2.N_C_MAX = res.N_C\
    GROUP BY res2.subcode, 	res2.NZ_TYPE, res2.N_C_MAX\
    )\
    SELECT res.SUBCODE,	res.SUBCODE || '/' || res.SUBNAME AS SUBNAME, res.POINTNAME, res.N_FON, \
    case when res.NZ_TYPE = 2 then res.N_C else NULL end as type2, \
    case when res.NZ_TYPE = 3 then res.N_C else NULL end as type3, \
    case when res.NZ_TYPE in (1,4) then res.N_C else NULL end as type4_1,\
    res.NZ_TYPE, res.IST_NN,	res.PRC, res.CECHNAME\
    FROM res\
    INNER JOIN res3\
    ON res3.subcode = res.subcode AND res3.NZ_TYPE = res.NZ_TYPE AND res3.N_C_MAX = res.N_C AND res3.PRC_MAX = res.PRC\
    ORDER BY res.subcode, replace(res.NZ_TYPE,1,5) \
    ;"

cur.execute(query)
df_tbl5=pd.DataFrame(cur.fetchall())

query = "WITH res as (\
    SELECT RESCODE.CODE AS subcode, SUBST.NAME AS subname, RASPOINT.CODE AS pointname, RESDATA.N_FON, RESDATA.N_C, RASPOINT.NZ_TYPE, IST.IST_NN, SRES.PRC, CECH.NAME AS cechname\
    FROM RESDATA\
    JOIN RESTYPE ON RESTYPE.ID = RESDATA.RESTYPE_ID\
    JOIN RASPOINT ON RASPOINT.ID = RESDATA.RASPOINT_ID\
    JOIN RESCODE ON RESCODE.ID = RESTYPE.RESCODE_ID\
    JOIN RESSHARE ON RESSHARE.RESDATA_ID = RESDATA.ID\
    JOIN SRES ON SRES.RESSHARE_ID = RESSHARE.ID\
    JOIN IST ON IST.ID = SRES.IST_ID\
    JOIN CECH ON CECH.ID = IST.CH_ID\
    JOIN SUBST ON SUBST.CODE = RESCODE.CODE\
    WHERE RESCODE.CVRUN_ID = " + str(calc_id_tbl5cc) + "\
    ),\
    res2 as(\
    SELECT subcode, NZ_TYPE, MAX(N_C) AS N_C_MAX\
    FROM res\
    GROUP BY subcode, NZ_TYPE\
    ),\
    res3 as(\
    SELECT res2.subcode, 	res2.NZ_TYPE, res2.N_C_MAX, max(res.PRC) AS PRC_MAX\
    FROM res\
    INNER JOIN res2\
    ON res2.subcode = res.subcode AND res2.NZ_TYPE = res.NZ_TYPE AND res2.N_C_MAX = res.N_C\
    GROUP BY res2.subcode, 	res2.NZ_TYPE, res2.N_C_MAX\
    )\
    SELECT res.SUBCODE,	res.SUBCODE || '/' || res.SUBNAME AS SUBNAME, res.POINTNAME, res.N_FON, \
    case when res.NZ_TYPE = 2 then res.N_C else NULL end as type2, \
    case when res.NZ_TYPE = 3 then res.N_C else NULL end as type3, \
    case when res.NZ_TYPE in (1,4) then res.N_C else NULL end as type4_1,\
    res.NZ_TYPE, res.IST_NN,	res.PRC, res.CECHNAME\
    FROM res\
    INNER JOIN res3\
    ON res3.subcode = res.subcode AND res3.NZ_TYPE = res.NZ_TYPE AND res3.N_C_MAX = res.N_C AND res3.PRC_MAX = res.PRC\
    ORDER BY res.subcode, replace(res.NZ_TYPE,1,5) \
    ;"

cur.execute(query)
df_tbl5cc=pd.DataFrame(cur.fetchall())

df_nmu_mr=df_tbl5[df_tbl5[6]>=0]
df_nmu_mr = df_nmu_mr.rename(columns={0:"substance_code"})
df_nmu_mr=pd.merge(df_subs_unique,df_nmu_mr,how='left',on='substance_code').sort_values(by=['substance_code'],ascending=True)
df_nmu_mr['m_r']=df_nmu_mr['PDKmr']
df_nmu_mr.loc[df_nmu_mr['m_r'] == 0,'m_r'] = df_nmu_mr['OBUV']
df_nmu_mr['mg_m3']=df_nmu_mr[6]*df_nmu_mr['PDKsg']
df_nmu_mr['pdk_p2']=df_nmu_mr[6]+df_nmu_mr[6]*0.2
df_nmu_mr['pdk_p4']=df_nmu_mr[6]+df_nmu_mr[6]*0.4
df_nmu_mr['pdk_p6']=df_nmu_mr[6]+df_nmu_mr[6]*0.6
#print(df_nmu_mr)

df_nmu_cc=df_tbl5cc[df_tbl5cc[6]>=0]
df_nmu_cc = df_nmu_cc.rename(columns={0:"substance_code"})
df_nmu_cc=pd.merge(df_subs_unique,df_nmu_cc,how='left',on='substance_code').sort_values(by=['substance_code'],ascending=True)
df_nmu_cc['m_r']=df_nmu_cc['PDKmr']
df_nmu_cc.loc[df_nmu_cc['m_r'] == 0,'m_r'] = df_nmu_mr['OBUV']
df_nmu_cc['mg_m3']=df_nmu_cc[6]*df_nmu_cc['PDKsg']
df_nmu_cc['pdk_p2']=df_nmu_cc[6]+df_nmu_cc[6]*0.2
df_nmu_cc['pdk_p4']=df_nmu_cc[6]+df_nmu_cc[6]*0.4
df_nmu_cc['pdk_p6']=df_nmu_cc[6]+df_nmu_cc[6]*0.6

with pd.ExcelWriter(filepathout,mode='w',engine='openpyxl',if_sheet_exists='replace') as writer:

    df_ishod_guide.to_excel(writer,sheet_name='tbl2_2',startrow=8,columns=['ceh_source','ceh_name_source','iv_subst','cnt_iv_subst','ch_day_year_subst','source_name','cnt_izav_source', \
                                                                           'source','rezhim_subst','height_source','diameter_source','speed_source','ob_r_source','T_source','x1_source', \
                                                                           'y1_source','x2_source','y2_source','width_source','ciklon_subst','obesp_subst','effect_subst','substance_code', \
                                                                           'name_quide','coef_os','g_s_subst','g_norm','t_year_subst','t_year_subst'])

    df_ishod_guide_2.to_excel(writer,sheet_name='tbl2',startrow=8,columns=['ceh_source','ceh_name_source','iv_subst','cnt_iv_subst','ch_day_year_subst','source_name','cnt_izav_source', \
                                                                           'source','rezhim_subst','height_source','diameter_source','speed_source','ob_r_source','T_source','x1_source', \
                                                                           'y1_source','x2_source','y2_source','width_source','ciklon_subst','obesp_subst','effect_subst','substance_code', \
                                                                           'name_quide','coef_os','g_s_subst','g_norm','t_year_subst','t_year_subst'])

    df_ishod_guide_norm.to_excel(writer,sheet_name='norm',startrow=8)

    df_ishod_guide_nenorm.to_excel(writer,sheet_name='nenorm',startrow=8)

    df_guide_tbl4.to_excel(writer,sheet_name='tbl4',startrow=8)

    df_guide_tbl6_all.to_excel(writer,sheet_name='tbl6',startrow=8)

    df_guide_tbl7.to_excel(writer,sheet_name='tbl7',startrow=8,columns=['name_quide','class_op','g_s_subst','t_year_subst','pdv'])

    df_tbl5.to_excel(writer,sheet_name='tbl5',startrow=8)

    df_nmu_mr.to_excel(writer,sheet_name='df_nmu_mr',startrow=8,columns=['substance_code','name_quide','m_r','PDKsg','mg_m3',6,'pdk_p2','pdk_p4','pdk_p6'])

    df_tbl5cc.to_excel(writer,sheet_name='tbl5cc',startrow=8)

    df_nmu_cc.to_excel(writer,sheet_name='df_nmu_cc',startrow=8,columns=['substance_code','name_quide','m_r','PDKsg','mg_m3',6,'pdk_p2','pdk_p4','pdk_p6'])

    df_ishod_guide_2.to_excel(writer,sheet_name='all',startrow=8)

    df_subs_unique.to_excel(writer,sheet_name='subs_unique',startrow=8)



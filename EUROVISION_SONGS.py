from pytube import YouTube
import os
import re

def sanitize_filename(title):
    # Replace invalid characters in the title with underscores
    invalid_chars = '\\/:*?"<>|'
    for char in invalid_chars:
        title = title.replace(char, '_')
    return title

def download_youtube_videos(urls, download_directory):
    for url in urls:
        try:
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()  # Get the highest resolution stream
            
            # Sanitize the video title for use in the filename
            title = sanitize_filename(yt.title)
            
            # Specify the download path with .mp4 extension
            download_path = os.path.join(download_directory, f"{title}.mp4")
            
            if not os.path.exists(download_directory):
                os.makedirs(download_directory)

            # Download the video
            video.download(output_path=download_directory, filename=f"{title}.mp4")
            print(f"Downloaded: {title}.mp4")
        except Exception as e:
            print(f"Error downloading video from {url}: {e}")




# URLs of YouTube videos to download

test = ['https://www.youtube.com/watch?v=nrjFhjpm7D8']
youtube_urls_2024 = ['https://www.youtube.com/watch?v=nrjFhjpm7D8', 'https://www.youtube.com/watch?v=_6xfmW0Fc40', 'https://www.youtube.com/watch?v=tJ2IaHxCvdw', 'https://www.youtube.com/watch?v=Kqda15G4T-4', 'https://www.youtube.com/watch?v=SUNM6dawXq8', 'https://www.youtube.com/watch?v=WCe9zrWEFNc', 'https://www.youtube.com/watch?v=EBsgTJQFl9k', 'https://www.youtube.com/watch?v=8q5QozrtEPA', 'https://www.youtube.com/watch?v=_iTcX6NlAqA', 'https://www.youtube.com/watch?v=3pCtdFnv9eQ', 'https://www.youtube.com/watch?v=zY6RbPaTNUc', 'https://www.youtube.com/watch?v=8Wi7fhswoBA', 'https://www.youtube.com/watch?v=tfoOop2HXxQ', 'https://www.youtube.com/watch?v=blMwY8Jabyk', 'https://www.youtube.com/watch?v=twhq3S4YHdQ', 'https://www.youtube.com/watch?v=uTYalXf184A', 'https://www.youtube.com/watch?v=OouUsCZ3xkM', 'https://www.youtube.com/watch?v=ZGRXRrlIspY', 'https://www.youtube.com/watch?v=lJYn09tuPw4', 'https://www.youtube.com/watch?v=OKzWskcTTA8', 'https://www.youtube.com/watch?v=8TIji6Ac8b4', 'https://www.youtube.com/watch?v=OrL668EQRu0', 'https://www.youtube.com/watch?v=HV3sORfrREE', 'https://www.youtube.com/watch?v=l6eS60n4wg8', 'https://www.youtube.com/watch?v=Jom9sNL5whs', 'https://www.youtube.com/watch?v=gT2wY0DjYGo', 'https://www.youtube.com/watch?v=UipzszlJwRQ', 'https://www.youtube.com/watch?v=IhvDkF9XZx0', 'https://www.youtube.com/watch?v=K5wDGhcDSpQ', 'https://www.youtube.com/watch?v=9NcAJtfhpWA', 'https://www.youtube.com/watch?v=lWzPO6nPpwU', 
'https://www.youtube.com/watch?v=uWcSsi7SliI', 'https://www.youtube.com/watch?v=zSZqlQZ0_us', 'https://www.youtube.com/watch?v=yekc8t0rJqA', 'https://www.youtube.com/watch?v=kiGDvM14Kwg', 'https://www.youtube.com/watch?v=k_8cNbF8FLI', 'https://www.youtube.com/watch?v=mvs92WfR8lM']

youtube_urls_2023 = ['https://www.youtube.com/watch?v=TI9rSDhXwyc', 'https://www.youtube.com/watch?v=h0q7AkYk2hY', 'https://www.youtube.com/watch?v=GSoy_mJMlMY', 'https://www.youtube.com/watch?v=8uk64V9h0Ko', 'https://www.youtube.com/watch?v=8BNtaW1IEtA', 'https://www.youtube.com/watch?v=U1xD14IMKtg', 'https://www.youtube.com/watch?v=hGuGfdEJ5Pw', 'https://www.youtube.com/watch?v=49YiimKeyDI', 'https://www.youtube.com/watch?v=ag8qxpvTTy0', 'https://www.youtube.com/watch?v=XVZvzZF1JOk', 'https://www.youtube.com/watch?v=HsbC-OYMA3s', 'https://www.youtube.com/watch?v=l6rS8Dv5g-8', 'https://www.youtube.com/watch?v=fOtQJ4o-HoA', 'https://www.youtube.com/watch?v=HNvGZeEQvfc', 'https://www.youtube.com/watch?v=dyGR4YWlPEs', 'https://www.youtube.com/watch?v=gJSZA0Zh2xU', 'https://www.youtube.com/watch?v=lzlTcA0OC5s', 'https://www.youtube.com/watch?v=80-4_rjW10U', 'https://www.youtube.com/watch?v=Z3mIcCllJXY', 'https://www.youtube.com/watch?v=d6IiOSut_4M', 'https://www.youtube.com/watch?v=SEykwl9X9SY', 'https://www.youtube.com/watch?v=QsgouAEd34U', 'https://www.youtube.com/watch?v=zVmVt9qmg9g', 'https://www.youtube.com/watch?v=SABOfYgGk8M', 'https://www.youtube.com/watch?v=3XAsam043OY', 'https://www.youtube.com/watch?v=PUHSM_vTqTI', 'https://www.youtube.com/watch?v=SEgF1aP-U1o', 'https://www.youtube.com/watch?v=HYfkxX4PFyw', 'https://www.youtube.com/watch?v=Bf3iPXU1RYU', 'https://www.youtube.com/watch?v=pIdHjcqyLfo', 'https://www.youtube.com/watch?v=gPRfg9wzbpw', 
'https://www.youtube.com/watch?v=3LXlPviGiWc', 'https://www.youtube.com/watch?v=Vw6qPWhjevk', 'https://www.youtube.com/watch?v=BE2Fj0W4jP4', 'https://www.youtube.com/watch?v=l4NDErv49mk', 'https://www.youtube.com/watch?v=I2oqDpefJ1s', 'https://www.youtube.com/watch?v=tvJEE2ryCRQ']

youtube_urls_2022 = ['https://www.youtube.com/watch?v=_jWXmo0-ZjI', 'https://www.youtube.com/watch?v=DAJ6vfmD_ic', 'https://www.youtube.com/watch?v=wosfFz2FJPU', 'https://www.youtube.com/watch?v=dMgjHYwXSuo', 'https://www.youtube.com/watch?v=tegPzHEL4ms', 'https://www.youtube.com/watch?v=sB09advfF6E', 'https://www.youtube.com/watch?v=EwZTI5AoTg4', 'https://www.youtube.com/watch?v=9vBQdtW3mJE', 'https://www.youtube.com/watch?v=W2IUdTl-gAI', 'https://www.youtube.com/watch?v=EGRzSefqOm0', 'https://www.youtube.com/watch?v=cVg6MpVR2Pw', 'https://www.youtube.com/watch?v=GdTpQmMem8U', 'https://www.youtube.com/watch?v=LSi9nfr65FE', 'https://www.youtube.com/watch?v=H1lcGXwOqJI', 'https://www.youtube.com/watch?v=zXiZAbqETvk', 'https://www.youtube.com/watch?v=2BYIou-oWXA', 'https://www.youtube.com/watch?v=BWeT0nJpB3Y', 'https://www.youtube.com/watch?v=G71c48O3j-s', 'https://www.youtube.com/watch?v=Kq2AJrWm04s', 'https://www.youtube.com/watch?v=XgXjPUsjx4Y', 'https://www.youtube.com/watch?v=blEy4xHuMbY', 'https://www.youtube.com/watch?v=TM0_0WfuxSk', 'https://www.youtube.com/watch?v=BVqSTVJhD44', 'https://www.youtube.com/watch?v=DFCFM5qtvms', 'https://www.youtube.com/watch?v=DUqf_zO2QaI', 'https://www.youtube.com/watch?v=L-ViRVRiGl0', 'https://www.youtube.com/watch?v=sgOnu7ux2-k', 'https://www.youtube.com/watch?v=zvOihqB4eKk', 'https://www.youtube.com/watch?v=adCU2rQyDeY', 'https://www.youtube.com/watch?v=jRVDZ6446eM', 'https://www.youtube.com/watch?v=mZtbD47u6yI', 
'https://www.youtube.com/watch?v=nPpuwy79sHs', 'https://www.youtube.com/watch?v=vCmX64N_sXM', 'https://www.youtube.com/watch?v=nBtQj1MfNYA', 'https://www.youtube.com/watch?v=S1tFqoflsT8', 'https://www.youtube.com/watch?v=jSQYTt4xg3I', 'https://www.youtube.com/watch?v=i777psA2gP4', 'https://www.youtube.com/watch?v=hq2HCmHv5p4', 'https://www.youtube.com/watch?v=F1fl60ypdLs', 'https://www.youtube.com/watch?v=RZ0hqX_92zI']

youtube_urls_2021 = ['https://www.youtube.com/watch?v=OxniMKVXjqM', 'https://www.youtube.com/watch?v=CoUTzNXQud0', 'https://www.youtube.com/watch?v=xV9_pKj8Df8', 'https://www.youtube.com/watch?v=FTQ22S5YC7Q', 'https://www.youtube.com/watch?v=HbpxcUMtjwY', 'https://www.youtube.com/watch?v=B1ZiPrMwMYA', 'https://www.youtube.com/watch?v=vKdxjoNluzY', 'https://www.youtube.com/watch?v=MgGc1F_cOE8', 'https://www.youtube.com/watch?v=cgGRCTUPsqY', 'https://www.youtube.com/watch?v=w2ytONrRyww', 'https://www.youtube.com/watch?v=mhMZQyv_Fhw', 'https://www.youtube.com/watch?v=fOPGxQ4fgVw', 'https://www.youtube.com/watch?v=Unj9WbeLzRU', 'https://www.youtube.com/watch?v=5qnogt74_F8', 'https://www.youtube.com/watch?v=1m0VEAfLV4E', 'https://www.youtube.com/watch?v=QhZhJFp0vVw', 'https://www.youtube.com/watch?v=YSMhu-PrLME', 'https://www.youtube.com/watch?v=FY2rxbZNvZ0', 'https://www.youtube.com/watch?v=5Y-blG5ptwo', 'https://www.youtube.com/watch?v=RVH5dn1cxAQ', 'https://www.youtube.com/watch?v=btA_Tyiyfhc', 'https://www.youtube.com/watch?v=JNweec5olYw', 'https://www.youtube.com/watch?v=jbbc2yKnv0M', 'https://www.youtube.com/watch?v=5I_1GTehgkI', 'https://www.youtube.com/watch?v=o3Da5cr2fTs', 'https://www.youtube.com/watch?v=WRcSHPb_Qwc', 'https://www.youtube.com/watch?v=F0r3vmGLzZU', 'https://www.youtube.com/watch?v=Uy6TeDNvSGo', 'https://www.youtube.com/watch?v=qq9SceXaukA', 'https://www.youtube.com/watch?v=5ZWcsj_6Log', 'https://www.youtube.com/watch?v=V-Di9A28e5E', 
'https://www.youtube.com/watch?v=TkhiH-JXFPs', 'https://www.youtube.com/watch?v=Q1lkpIqf7a4', 'https://www.youtube.com/watch?v=J9jWDxKQ50s', 'https://www.youtube.com/watch?v=thV-vhOQHvQ', 'https://www.youtube.com/watch?v=NyJRyif6_kk', 'https://www.youtube.com/watch?v=jznH_fltcYA', 'https://www.youtube.com/watch?v=lqvzDkgok_g', 'https://www.youtube.com/watch?v=VxNOynEJ6wc']

youtube_urls_2020 = ['https://www.youtube.com/watch?v=vXpCWFIY6YE', 'https://www.youtube.com/watch?v=XpQHGMM8c5U', 'https://www.youtube.com/watch?v=gr-wWxu4974', 'https://www.youtube.com/watch?v=cOuiTJlBC50', 'https://www.youtube.com/watch?v=I0VzBCvO1Wk', 'https://www.youtube.com/watch?v=F0wfxz5zq04', 'https://www.youtube.com/watch?v=lAqjksxc4iA', 'https://www.youtube.com/watch?v=V_hgYnwZR8I', 'https://www.youtube.com/watch?v=2rOwScdxjJU', 'https://www.youtube.com/watch?v=Jl_qEw_4OK0', 'https://www.youtube.com/watch?v=wROqCHLnbko', 'https://www.youtube.com/watch?v=XQ5tMhQIp1E', 'https://www.youtube.com/watch?v=3EIQ6U039ms', 'https://www.youtube.com/watch?v=EgONBKFQpxE', 'https://www.youtube.com/watch?v=J5SOdhXjYko', 'https://www.youtube.com/watch?v=LjNK4Xywjc4', 'https://www.youtube.com/watch?v=hAobDQ9GbT4', 'https://www.youtube.com/watch?v=dJxCINWp_j0', 'https://www.youtube.com/watch?v=1HU7ocv3S2o', 'https://www.youtube.com/watch?v=HLgE0Ayl5Hc', 'https://www.youtube.com/watch?v=YjzyZZ-oidc', 'https://www.youtube.com/watch?v=TA57rugucwk', 'https://www.youtube.com/watch?v=ELr6U2fOrnE', 'https://www.youtube.com/watch?v=FxPm-Wz8qpY', 'https://www.youtube.com/watch?v=CFCn_8oViRw', 'https://www.youtube.com/watch?v=RnD1ApDo5_k', 'https://www.youtube.com/watch?v=sMcxWB90TTY', 'https://www.youtube.com/watch?v=xPZumQQExQc', 'https://www.youtube.com/watch?v=o9atJbnqhJU', 'https://www.youtube.com/watch?v=s_Y7mMka4SQ', 'https://www.youtube.com/watch?v=eIZ48w4epng', 
'https://www.youtube.com/watch?v=TmqSU3v_Mtw', 'https://www.youtube.com/watch?v=L_dWvTCdDQ4', 'https://www.youtube.com/watch?v=c6ZNo_hVA6E', 'https://www.youtube.com/watch?v=7fqZevYLUMs', 'https://www.youtube.com/watch?v=weLeotNwexg', 'https://www.youtube.com/watch?v=zuDdex1st-Y', 'https://www.youtube.com/watch?v=7EpSBDPlZn4', 'https://www.youtube.com/watch?v=O9GAfFHZE-E', 'https://www.youtube.com/watch?v=zNetXPSld50', 'https://www.youtube.com/watch?v=6iS-lV909T4']

youtube_urls_2019 = ['https://www.youtube.com/watch?v=-NAbYUoxIfg', 'https://www.youtube.com/watch?v=avBwSUYlTtI', 'https://www.youtube.com/watch?v=Eo5H62mCIsg', 'https://www.youtube.com/watch?v=FVSZDF9O-bA', 'https://www.youtube.com/watch?v=D6vvuCiHwSs', 'https://www.youtube.com/watch?v=C1Y9LBusHzA', 'https://www.youtube.com/watch?v=iFB9NnjU4ns', 'https://www.youtube.com/watch?v=gXT5E8kUgfs', 'https://www.youtube.com/watch?v=wIpEI-NhRxg', 'https://www.youtube.com/watch?v=NJxLKFZKhNs', 'https://www.youtube.com/watch?v=mucmvTLHJQM', 'https://www.youtube.com/watch?v=PppvSl3_W4E', 'https://www.youtube.com/watch?v=VSPhIwOJfRs', 'https://www.youtube.com/watch?v=AjZNbIQtWvw', 'https://www.youtube.com/watch?v=vu4nHsaAJwU', 'https://www.youtube.com/watch?v=yFbSj_yPCPM', 'https://www.youtube.com/watch?v=5pQV_-40m_U', 'https://www.youtube.com/watch?v=IpVr0pBLfI4', 'https://www.youtube.com/watch?v=kTb69WkBbvs', 'https://www.youtube.com/watch?v=lX7DT9GMHQM', 'https://www.youtube.com/watch?v=uCdS42uCqP0', 'https://www.youtube.com/watch?v=M-aoyPa41Ic', 'https://www.youtube.com/watch?v=NCtKU3m3R-8', 'https://www.youtube.com/watch?v=5Nb3HMzsfZY', 'https://www.youtube.com/watch?v=H-byNyainRA', 'https://www.youtube.com/watch?v=-mo207V5Z2o', 'https://www.youtube.com/watch?v=oV200JAouTc', 'https://www.youtube.com/watch?v=R3D-r4ogr7s', 'https://www.youtube.com/watch?v=0pAURAsum4A', 'https://www.youtube.com/watch?v=Ovt7YGHAj8I', 'https://www.youtube.com/watch?v=IEu0F5uobVo', 
'https://www.youtube.com/watch?v=SIGn9_yMLn4', 'https://www.youtube.com/watch?v=cZC9o_Z90yo', 'https://www.youtube.com/watch?v=eNzlxEZ_JG4', 'https://www.youtube.com/watch?v=d_iEis_ZRoQ', 'https://www.youtube.com/watch?v=X0mdaeAyPvA', 'https://www.youtube.com/watch?v=vGtPNQ6g6Ng', 'https://www.youtube.com/watch?v=lWXuohnM14U', 'https://www.youtube.com/watch?v=oEdWkdVKIqQ', 'https://www.youtube.com/watch?v=8aUYzqAIdoM', 'https://www.youtube.com/watch?v=HV-eOhTS8Dw']

youtube_urls_2018 = ['https://www.youtube.com/watch?v=uyl1b1fVmdU', 'https://www.youtube.com/watch?v=CYlWiHjUK0c', 'https://www.youtube.com/watch?v=2BBLTY6T2Ck', 'https://www.youtube.com/watch?v=a8Yvzo1puoE', 'https://www.youtube.com/watch?v=1CUwlpqUuvA', 'https://www.youtube.com/watch?v=ywy_y24v_ao', 'https://www.youtube.com/watch?v=Z2cZE2gCfWg', 'https://www.youtube.com/watch?v=vC-1tdGDFQc', 'https://www.youtube.com/watch?v=YxBLFbW5BqE', 'https://www.youtube.com/watch?v=vyDTbJ4wenY', 'https://www.youtube.com/watch?v=w0ZUuQe0shk', 'https://www.youtube.com/watch?v=c0kP074Mw0k', 'https://www.youtube.com/watch?v=ImawXdXIGd8', 'https://www.youtube.com/watch?v=hdjiuCUUpPc', 'https://www.youtube.com/watch?v=vjLuTtUv0Ns', 'https://www.youtube.com/watch?v=FvVx5-mzmm0', 'https://www.youtube.com/watch?v=N4YwSy4Q9k0', 'https://www.youtube.com/watch?v=-XOR1DhtDC0', 'https://www.youtube.com/watch?v=p6e1TmYb33w', 'https://www.youtube.com/watch?v=RQytWeg9CzE', 'https://www.youtube.com/watch?v=QD1cQ2wZ1dk', 'https://www.youtube.com/watch?v=84LBjXaeKk4', 'https://www.youtube.com/watch?v=81M-mp5t8uM', 'https://www.youtube.com/watch?v=KGxANwWKz3U', 'https://www.youtube.com/watch?v=pPDFhfU25go', 'https://www.youtube.com/watch?v=d52ViPImdls', 'https://www.youtube.com/watch?v=5evrVL1rJPA', 'https://www.youtube.com/watch?v=XEi080yOuB8', 'https://www.youtube.com/watch?v=p7jHz5asMs8', 'https://www.youtube.com/watch?v=MV_cR_Qb2Cg', 'https://www.youtube.com/watch?v=N17BdRwOvBA', 
'https://www.youtube.com/watch?v=oyoiCyP4Bkg', 'https://www.youtube.com/watch?v=mHjGbADMcOI', 'https://www.youtube.com/watch?v=DGR4S3y7qcw', 'https://www.youtube.com/watch?v=KujGHwyfMWM', 'https://www.youtube.com/watch?v=66D0pKVdA-4', 'https://www.youtube.com/watch?v=WRQWQShbPHU', 'https://www.youtube.com/watch?v=fBU0_hfST_o', 'https://www.youtube.com/watch?v=28oMEFgSoyk', 'https://www.youtube.com/watch?v=z101xtUBflU', 'https://www.youtube.com/watch?v=wJGTVsluHkw', 'https://www.youtube.com/watch?v=lhOuMYtQ94M', 'https://www.youtube.com/watch?v=8dmlXBBC6J8']

youtube_urls_2017 = ['https://www.youtube.com/watch?v=NyKOBMAXFFA', 'https://www.youtube.com/watch?v=g373Libigw8', 'https://www.youtube.com/watch?v=YTCP4S1dqwA', 'https://www.youtube.com/watch?v=gJIjZF5sgzg', 'https://www.youtube.com/watch?v=g_HSRHqd_7s', 'https://www.youtube.com/watch?v=coFfFZvPmRY', 'https://www.youtube.com/watch?v=oxsCmChDYwA', 'https://www.youtube.com/watch?v=OMmm-G078LM', 'https://www.youtube.com/watch?v=4Sya_GIxsw0', 'https://www.youtube.com/watch?v=ZDe9FCLgE04', 'https://www.youtube.com/watch?v=-KT8_ZOHAXE', 'https://www.youtube.com/watch?v=vUbGnq8maS0', 'https://www.youtube.com/watch?v=NxqPpzWYN1c', 'https://www.youtube.com/watch?v=Ufba0nOz0fQ', 'https://www.youtube.com/watch?v=HjiLKsLQl4I', 'https://www.youtube.com/watch?v=agSS_a3ccgA', 'https://www.youtube.com/watch?v=t1KKjykH6fw', 'https://www.youtube.com/watch?v=iO14p2uCzkM', 'https://www.youtube.com/watch?v=hqM0AkP7zcI', 'https://www.youtube.com/watch?v=UPlm18-AlGg', 'https://www.youtube.com/watch?v=EOpZikqrfOA', 'https://www.youtube.com/watch?v=YapnW_zfWJk', 'https://www.youtube.com/watch?v=KieE_MLv-ZY', 'https://www.youtube.com/watch?v=Vxos6ceOrRA', 'https://www.youtube.com/watch?v=-7WpnSMEPjc', 'https://www.youtube.com/watch?v=tGctKNrfn8M', 'https://www.youtube.com/watch?v=SWaQdHoCvYk', 'https://www.youtube.com/watch?v=rQ1BXJpfa4I', 'https://www.youtube.com/watch?v=_9XsCqGg8ls', 'https://www.youtube.com/watch?v=XvIbLOOWfYI', 'https://www.youtube.com/watch?v=U-Bk0PCotY0', 
'https://www.youtube.com/watch?v=xVCokUW3BUo', 'https://www.youtube.com/watch?v=Qotooj7ODCM', 'https://www.youtube.com/watch?v=ZSHc7iDuBCQ', 'https://www.youtube.com/watch?v=UC7QzXPnt6k', 'https://www.youtube.com/watch?v=A0wAd-a0hXA', 'https://www.youtube.com/watch?v=vbGub2klcV4', 'https://www.youtube.com/watch?v=qAOXHdLdlqQ', 'https://www.youtube.com/watch?v=RjH_4oYqLw4', 'https://www.youtube.com/watch?v=OrNPRfS9Sbg', 'https://www.youtube.com/watch?v=mogNLkIEI0k', 'https://www.youtube.com/watch?v=Fl1GYTg4GmA']

youtube_urls_2016 = ['https://www.youtube.com/watch?v=jdT5EGcTjYw', 'https://www.youtube.com/watch?v=nL066Rp7J7k', 'https://www.youtube.com/watch?v=5ymFX91HwM0', 'https://www.youtube.com/watch?v=3xuPYt5i5cE', 'https://www.youtube.com/watch?v=cB8eSLyffsI', 'https://www.youtube.com/watch?v=pM07r57QqGg', 'https://www.youtube.com/watch?v=xDBjhAGaeWg', 'https://www.youtube.com/watch?v=QLrXmTB8OaY', 'https://www.youtube.com/watch?v=PQqUTigWKHY', 'https://www.youtube.com/watch?v=8QUM-_EbE2o', 'https://www.youtube.com/watch?v=idUxTqmCFR0', 'https://www.youtube.com/watch?v=wVy3rTNSN4Y', 'https://www.youtube.com/watch?v=jGz12i-wGd0', 'https://www.youtube.com/watch?v=g0-j0Eh8VNA', 'https://www.youtube.com/watch?v=oAQIPxgQkM8', 'https://www.youtube.com/watch?v=-aLPsiyavcU', 'https://www.youtube.com/watch?v=rviE2-9eiTI', 'https://www.youtube.com/watch?v=bHDHi37bboE', 'https://www.youtube.com/watch?v=55ubbjAzwYA', 'https://www.youtube.com/watch?v=bT2DcpqvorI', 'https://www.youtube.com/watch?v=6osxLLPLUDk', 'https://www.youtube.com/watch?v=ezJsUMD-y-I', 'https://www.youtube.com/watch?v=SS5TB2XUdgs', 'https://www.youtube.com/watch?v=YfnhDfy8AjU', 'https://www.youtube.com/watch?v=o-2Lt7zzlBU', 'https://www.youtube.com/watch?v=O1wS7NNCo38', 'https://www.youtube.com/watch?v=58YS5m3EYVY', 'https://www.youtube.com/watch?v=LlhV-E6leTI', 'https://www.youtube.com/watch?v=FgKehisElQI', 'https://www.youtube.com/watch?v=PwF9DI89q1w', 'https://www.youtube.com/watch?v=uIIzwFoE6ME', 
'https://www.youtube.com/watch?v=ACLcqZMwCSo', 'https://www.youtube.com/watch?v=87BBmxm7IJU', 'https://www.youtube.com/watch?v=e94dst20C9Y', 'https://www.youtube.com/watch?v=HzPkDb2FSeg', 'https://www.youtube.com/watch?v=yTlxLiSQWjk', 'https://www.youtube.com/watch?v=ulI3F1T82is', 'https://www.youtube.com/watch?v=EgbjNsxehrY', 'https://www.youtube.com/watch?v=2AIPrVchJN8', 'https://www.youtube.com/watch?v=HZI0_aR7BuA', 'https://www.youtube.com/watch?v=B-rnM-MwRHY', 'https://www.youtube.com/watch?v=XgGahKsBtts']


youtube_urls_2015 = ['https://www.youtube.com/watch?v=fsH9iVaZSaA', 'https://www.youtube.com/watch?v=BYXr2FccjKE', 'https://www.youtube.com/watch?v=H0EhhZWXTng', 'https://www.youtube.com/watch?v=-f993p0CAV8', 'https://www.youtube.com/watch?v=L_y-yMIzTNc', 'https://www.youtube.com/watch?v=Cwjm1lRV4N4', 'https://www.youtube.com/watch?v=G48p8eNhnd8', 'https://www.youtube.com/watch?v=RUNEoMBLGc8', 'https://www.youtube.com/watch?v=SLz6VeSPXjA', 'https://www.youtube.com/watch?v=J--Tgi_iZQ8', 'https://www.youtube.com/watch?v=Xsx_dIJOtgI', 'https://www.youtube.com/watch?v=v4Y0HOPL5GU', 'https://www.youtube.com/watch?v=tJful-Jtc9o', 'https://www.youtube.com/watch?v=ddC8lviTERI', 'https://www.youtube.com/watch?v=DGMJOchTRPc', 'https://www.youtube.com/watch?v=1RZ2JGC9Nlw', 'https://www.youtube.com/watch?v=MdybVsBESQc', 'https://www.youtube.com/watch?v=0Jl-Hr137uM', 'https://www.youtube.com/watch?v=3B5sdNJF0lk', 'https://www.youtube.com/watch?v=5bi1lK91bas', 'https://www.youtube.com/watch?v=1TOMqZV2jA8', 'https://www.youtube.com/watch?v=-usdXbeGHi8', 'https://www.youtube.com/watch?v=xtB_slM63JA', 'https://www.youtube.com/watch?v=SaJxu3vorLc', 'https://www.youtube.com/watch?v=px1MoZ0k7qY', 'https://www.youtube.com/watch?v=vrYmyTJ87vI', 'https://www.youtube.com/watch?v=O_fs4SPGyF0', 'https://www.youtube.com/watch?v=TtSum7ouImU', 'https://www.youtube.com/watch?v=oVKJK9yb5xY', 'https://www.youtube.com/watch?v=VBI8TQXi--M', 'https://www.youtube.com/watch?v=vE-LqXkb0ok', 
'https://www.youtube.com/watch?v=o7iOFkEymXA', 'https://www.youtube.com/watch?v=Q2gbKglCL5s', 'https://www.youtube.com/watch?v=FE1KJYNvVAE', 'https://www.youtube.com/watch?v=gXGo70i94S8', 'https://www.youtube.com/watch?v=y1c7gDOaFY0', 'https://www.youtube.com/watch?v=NsMiJJlElAY', 'https://www.youtube.com/watch?v=5sGOwFVUU0I', 'https://www.youtube.com/watch?v=ya1r_nFHiCQ', 'https://www.youtube.com/watch?v=Ethyx4A5ajM']


youtube_urls_2014 = ['https://www.youtube.com/watch?v=Ahu_K_Jh2vc', 'https://www.youtube.com/watch?v=oj0oOV-2fRQ', 'https://www.youtube.com/watch?v=xhCC_PN9UlA', 'https://www.youtube.com/watch?v=5mPUMPcFQAY', 'https://www.youtube.com/watch?v=tImGMW-4eHY', 'https://www.youtube.com/watch?v=wr3m4ghnq6w', 'https://www.youtube.com/watch?v=jnCTsJkieY4', 'https://www.youtube.com/watch?v=wi9Q1ufjooE', 'https://www.youtube.com/watch?v=3FDWaFfo1CU', 'https://www.youtube.com/watch?v=vjkqciwP034', 'https://www.youtube.com/watch?v=0v69AvCQJQY', 'https://www.youtube.com/watch?v=BFuGH2Kp9dI', 'https://www.youtube.com/watch?v=c9y6A1uXLn8', 'https://www.youtube.com/watch?v=T_RxJZ3N9kE', 'https://www.youtube.com/watch?v=U2qAvGsiCmc', 'https://www.youtube.com/watch?v=J9zEybTMeEs', 'https://www.youtube.com/watch?v=acOZVEN5XjE', 'https://www.youtube.com/watch?v=8W5ZlalAMV8', 'https://www.youtube.com/watch?v=h0D1Ya3NBQs', 'https://www.youtube.com/watch?v=qOGEtw7tmik', 'https://www.youtube.com/watch?v=E_hT08vzHt8', 'https://www.youtube.com/watch?v=l9ZfGttI4P0', 'https://www.youtube.com/watch?v=6FJtzRSKHKg', 'https://www.youtube.com/watch?v=4ggBPAm5XLA', 'https://www.youtube.com/watch?v=2BqLPMF8Xdc', 'https://www.youtube.com/watch?v=BTMli8U17MM', 'https://www.youtube.com/watch?v=VJ920cN2HmA', 'https://www.youtube.com/watch?v=fhMbHLiEjS4', 'https://www.youtube.com/watch?v=cAMpVodhiS4', 'https://www.youtube.com/watch?v=BCNN1JAgWqk', 'https://www.youtube.com/watch?v=_eZNTBJ-Hyc', 
'https://www.youtube.com/watch?v=CiwM1sY3u0s', 'https://www.youtube.com/watch?v=LY4n5FUlfDQ', 'https://www.youtube.com/watch?v=5PQJI-3LW-8', 'https://www.youtube.com/watch?v=DqjoM8ZlyMc', 'https://www.youtube.com/watch?v=slHboKF9PIQ', 'https://www.youtube.com/watch?v=C6w7tmWvm6M']

youtube_urls_2013 = ['https://www.youtube.com/watch?v=3u5Se-vJ6MA', 'https://www.youtube.com/watch?v=UGOSZ7Uufno', 'https://www.youtube.com/watch?v=gOJHi6JiKpY', 'https://www.youtube.com/watch?v=S7C3S2zuVp8', 'https://www.youtube.com/watch?v=XKewBfUE2Mg', 'https://www.youtube.com/watch?v=dCl7OUFNSCA', 'https://www.youtube.com/watch?v=Cb46Mhy_mCI', 'https://www.youtube.com/watch?v=FYm4sGd-qP0', 'https://www.youtube.com/watch?v=Ekx8mT-fR80', 'https://www.youtube.com/watch?v=QxVWcDevKLg', 'https://www.youtube.com/watch?v=Ooo6GvZNLhI', 'https://www.youtube.com/watch?v=dlBXOveVh7c', 'https://www.youtube.com/watch?v=hQwiQj5Dyj8', 'https://www.youtube.com/watch?v=-n3mwx0vQDE', 'https://www.youtube.com/watch?v=3HYTd7WDCPg', 'https://www.youtube.com/watch?v=LFs9AdNV4Qw', 'https://www.youtube.com/watch?v=rOimfHq76xk', 'https://www.youtube.com/watch?v=GzE88IYzXLI', 'https://www.youtube.com/watch?v=4tgtyl_5x5Y', 'https://www.youtube.com/watch?v=BjbcD72OaI4', 'https://www.youtube.com/watch?v=S8oaxDV1q6o', 'https://www.youtube.com/watch?v=xze_ilAXwWE', 'https://www.youtube.com/watch?v=0VLhnzk_dAs', 'https://www.youtube.com/watch?v=VK4TvZeL6c0', 'https://www.youtube.com/watch?v=xckgLUv73Jc', 'https://www.youtube.com/watch?v=FR9rtB2ilZU', 'https://www.youtube.com/watch?v=n5iazXvMw5o', 'https://www.youtube.com/watch?v=Vi1VYsOUCsY', 'https://www.youtube.com/watch?v=tc6a4EV63uM', 'https://www.youtube.com/watch?v=VgHWFiavqjA', 'https://www.youtube.com/watch?v=wHNwk3Oez8U', 
'https://www.youtube.com/watch?v=YirZIBi2vnY', 'https://www.youtube.com/watch?v=DbAAFijZIxE', 'https://www.youtube.com/watch?v=I2_zGcuEuwU', 'https://www.youtube.com/watch?v=5o_DnM_ANF8', 'https://www.youtube.com/watch?v=vtjdTPnCcu0', 'https://www.youtube.com/watch?v=Ba6ovg4yAto', 'https://www.youtube.com/watch?v=xgLCBm8Txsc', 'https://www.youtube.com/watch?v=-agn-ERgTXA']




# Directory to save the downloaded videos
download_directory = "g:/Euro Vision Songs/2024"
if not os.path.exists(download_directory):          
    download_youtube_videos(youtube_urls_2024, download_directory)


download_directory = "g:/Euro Vision Songs/2023"
if not os.path.exists(download_directory): 
    download_youtube_videos(youtube_urls_2023, download_directory)


download_directory = "g:/Euro Vision Songs/2022"
if not os.path.exists(download_directory): 
    download_youtube_videos(youtube_urls_2022, download_directory)


download_directory = "g:/Euro Vision Songs/2021"
if not os.path.exists(download_directory): 
    download_youtube_videos(youtube_urls_2021, download_directory)

download_directory = "g:/Euro Vision Songs/2020"
if not os.path.exists(download_directory): 
    download_youtube_videos(youtube_urls_2020, download_directory)


download_directory = "g:/Euro Vision Songs/2019"
if not os.path.exists(download_directory): 
    download_youtube_videos(youtube_urls_2019, download_directory)


download_directory = "g:/Euro Vision Songs/2018"
if not os.path.exists(download_directory): 
    download_youtube_videos(youtube_urls_2018, download_directory)

download_directory = "g:/Euro Vision Songs/2017"
if not os.path.exists(download_directory): 
    download_youtube_videos(youtube_urls_2017, download_directory)


download_directory = "g:/Euro Vision Songs/2016"
if not os.path.exists(download_directory): 
    download_youtube_videos(youtube_urls_2016, download_directory)


download_directory = "g:/Euro Vision Songs/2015"
if not os.path.exists(download_directory): 
    download_youtube_videos(youtube_urls_2015, download_directory)


download_directory = "g:/Euro Vision Songs/2014"
if not os.path.exists(download_directory): 
    download_youtube_videos(youtube_urls_2014, download_directory)


download_directory = "g:/Euro Vision Songs/2013"
if not os.path.exists(download_directory):  
    download_youtube_videos(youtube_urls_2013, download_directory)

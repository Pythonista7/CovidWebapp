import geopandas as gpd
import pandas as pd
import keplergl

class Covid_Mapper():
    
    def __init__(self):
        with open('BBMP.GeoJSON', 'r') as f:
            self.geojson = f.read()

        self.time_series=pd.read_csv('final_TS.csv',index_col="Unnamed: 0")
        self.gdf=gpd.read_file('BBMP.GeoJSON')
        self.gdf['WARD_NO']=self.gdf['WARD_NO'].astype(int)
        self.gdf.set_index('WARD_NO',inplace=True)
        self.gdf.sort_index(inplace=True)
    
    def get_for_day(self,i):
        final=gpd.GeoDataFrame(self.time_series[[i]].join(self.gdf[['LAT','LON','geometry']]))
        final.columns=["data","Lat","Lon","geometry"]
        map_1 = keplergl.KeplerGl(height=600)
        map_1.add_data(self.geojson,"geoj")
        map_1.add_data(final,name='final')
        map_1.save_to_html(file_name="templates/serve.html")
    
    def get_ward_info(self,no):
        dday=pd.read_csv('dday_ward.csv')
        dday.columns=columns=['ward_no','peak_day']
        ward_no,dd=dday.iloc[int(no)-1].values.tolist()
        return ward_no,dd
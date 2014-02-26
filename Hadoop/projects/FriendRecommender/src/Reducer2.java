import java.io.IOException;
import java.util.Iterator;
import java.util.Vector;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reducer;
import org.apache.hadoop.mapred.Reporter;


public class Reducer2 extends MapReduceBase implements Reducer<Text,Text,Text,Text> {

	@Override
	public void reduce(Text key, Iterator<Text> values,
			OutputCollector<Text, Text> output, Reporter reporter)
			throws IOException {
		
		final int TOP = 10;
		Vector<int[]> commonFriends = new Vector<>(TOP);
		
		while(values.hasNext()){
			String value = values.next().toString();
			
			String[] valueArray = value.split("-");
			if(valueArray.length>1){
				int[] pair = new int[2];
				pair[0] = Integer.parseInt( valueArray[0]);
				pair[1] = Integer.parseInt( valueArray[1]);
				boolean inserted = false;
				
				for(int i=0;i<commonFriends.size();i++){
					
					if(pair[1]>commonFriends.get(i)[1]){
						commonFriends.insertElementAt(pair, i);
						inserted = true;
						break;
					}
				}
				
				if(!inserted && commonFriends.size()<10){
					commonFriends.add(pair);
				}
			}
		}
		
		String recommend= "";
		for (int[] pair : commonFriends) {
			
			recommend += pair[0] + ",";
		}
		//to remove the last comma(,) for the string
		recommend = recommend.substring(0, recommend.length()-1);
		//write it to the output
		output.collect(key, new Text(recommend));
	}

}

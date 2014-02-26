import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Vector;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.Mapper;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reporter;


public class Mapper1 extends MapReduceBase implements Mapper<LongWritable,Text,Text,IntWritable> {


	@Override
	public void map(LongWritable key, Text value, OutputCollector<Text,IntWritable> output,
			Reporter reporter) throws IOException {
		
		String line = value.toString();
		
		int index = line.indexOf("\t");
		if( index == -1)
			return;
		
		String user_id = line.substring(0,index);
		StringTokenizer tokenizer = new StringTokenizer(line.substring(index+1), ",");
		Vector<String> friend_ids = new Vector<String>(tokenizer.countTokens());
		
		while(tokenizer.hasMoreTokens()){
			friend_ids.add(tokenizer.nextToken());
		}
		
		for (String friend : friend_ids) {
			output.collect( new Text(user_id +"-" + friend), new IntWritable(0));
		}
		
		for (String friend : friend_ids) {
			for (String mutalFriend : friend_ids) {
				if(friend == mutalFriend) continue;
				output.collect( new Text(friend +"-" + mutalFriend), new IntWritable(1));
			}
		}
		
	}

}

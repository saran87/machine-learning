import java.io.IOException;
import java.util.StringTokenizer;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.Mapper;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reporter;


public class Mapper2 extends MapReduceBase implements Mapper<LongWritable,Text,Text,Text> {


	@Override
	public void map(LongWritable key, Text value, OutputCollector<Text,Text> output,
			Reporter reporter) throws IOException {
		
		String line = value.toString();
		
		int index = line.indexOf("-");
		if( index == -1)
			return;
		index = line.indexOf("\t");
		if( index == -1)
			return;
		
		String friends = line.substring(0,index);
		String commonFriends = line.substring(index+1);
		
		StringTokenizer tokenizer = new StringTokenizer(friends, "-");
		
		
		while(tokenizer.hasMoreTokens()){
			output.collect( new Text(tokenizer.nextToken()), new Text(tokenizer.nextToken()+"-"+commonFriends));
		}	
	}

}

import java.io.IOException;
import java.util.Iterator;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reducer;
import org.apache.hadoop.mapred.Reporter;


public class Reducer1 extends MapReduceBase implements Reducer<Text,IntWritable,Text,IntWritable> {

	@Override
	public void reduce(Text key, Iterator<IntWritable> values,
			OutputCollector<Text, IntWritable> output, Reporter reporter)
			throws IOException {
		// TODO Auto-generated method stub
		int sum = 0, prod = 1;
		while(values.hasNext()){
			int value = values.next().get();
			sum  += value;
			prod *= value;
			if(prod == 0){
				//the users are already friends, so break
				break;
			}
		}
		
		if(prod != 0){
			output.collect(key, new IntWritable(sum));
		}
	}

}

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.FileInputFormat;
import org.apache.hadoop.mapred.FileOutputFormat;
import org.apache.hadoop.mapred.JobClient;
import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.mapred.RunningJob;
import org.apache.hadoop.mapred.TextInputFormat;
import org.apache.hadoop.mapred.TextOutputFormat;



public class Main {

	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		
		Configuration conf = new Configuration();
		JobConf job = new JobConf(conf);
		job.setJobName("RecommendFriend -1");
		
		job.setJarByClass(Main.class);
		
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);
		
		job.setMapOutputKeyClass(Text.class);
		job.setMapOutputValueClass(IntWritable.class);
		
		job.setMapperClass(Mapper1.class);
		job.setReducerClass(Reducer1.class);
		
		job.setInputFormat(TextInputFormat.class);
		job.setOutputFormat(TextOutputFormat.class);
		
		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));
		RunningJob runJob = JobClient.runJob(job);
		runJob.waitForCompletion();
		
		JobConf job2 = new JobConf(conf);
		job2.setJobName("RecommendFriend -2");
		
		job2.setJarByClass(Main.class);
		
		job2.setOutputKeyClass(Text.class);
		job2.setOutputValueClass(Text.class);
		
		job2.setMapOutputKeyClass(Text.class);
		job2.setMapOutputValueClass(Text.class);
		
		job2.setMapperClass(Mapper2.class);
		job2.setReducerClass(Reducer2.class);
		
		job2.setInputFormat(TextInputFormat.class);
		job2.setOutputFormat(TextOutputFormat.class);
		
		FileInputFormat.addInputPath(job2, new Path(args[1]));
		FileOutputFormat.setOutputPath(job2, new Path(args[2]));
		JobClient.runJob(job2);
	}

}

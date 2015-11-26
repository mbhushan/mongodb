import com.mongodb.MongoClient;
import com.mongodb.client.MongoDatabase;


public class MongoTestClient {

	private static String HOST = "localhost";
	private static int PORT = 27017;
	private static MongoClient mongoClient = null;
	
	public static void main(String [] args) {
		
	}
	
	public static void initMongoClient() {
		mongoClient = new MongoClient(HOST, PORT);
		MongoDatabase mdb = mongoClient.getDatabase("learn");
	}
}

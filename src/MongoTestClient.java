import java.util.HashMap;
import java.util.Map;

import org.bson.Document;

import com.mongodb.BasicDBObject;
import com.mongodb.MongoClient;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;



public class MongoTestClient {

	private static String HOST = "localhost";
	private static int PORT = 27017;
	private static MongoClient mongoClient = new MongoClient(HOST, PORT);;
	private static MongoDatabase db = mongoClient.getDatabase("learn");;
	private static MongoCollection<Document> collection = db.getCollection("unicrons");
	
	public static void main(String [] args) {
		
	}
	
	
	public static void insertDocuements() {
		Map<String, Object> documentMap = new HashMap<String, Object>();
		documentMap.put("database", "mkyongDB");
		documentMap.put("table", "hosting");

		Map<String, Object> documentMapDetail = new HashMap<String, Object>();
		documentMapDetail.put("records", "99");
		documentMapDetail.put("index", "vps_index1");
		documentMapDetail.put("active", "true");

		documentMap.put("detail", documentMapDetail);

		collection.insertOne(new Document(documentMap));
		collection.i
	}
}

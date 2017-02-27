class CreateTopics < ActiveRecord::Migration[5.0]
  def change
    create_table :topics do |t|
      t.string  :name
      t.integer :topic_id
      t.string  :description
      t.string  :uri
      t.string  :type

      t.timestamps
    end
  end
end

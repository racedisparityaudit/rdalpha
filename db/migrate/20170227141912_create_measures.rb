class CreateMeasures < ActiveRecord::Migration[5.0]
  def change
    create_table :measures do |t|
      t.string  :name
      t.integer :topic_id
      t.string  :description
      t.string  :uri
      t.string  :source
      t.string  :display
      t.string  :subtitle

      t.timestamps
    end
  end
end
